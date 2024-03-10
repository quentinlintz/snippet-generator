from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


@app.route("/generate-snippet", methods=["POST"])
def generate_snippet():
    data = request.json
    language = data.get("language")
    task = data.get("task")

    llm = OpenAI()
    code_prompt = PromptTemplate(
        template="Write a very short {language} function that will {task}",
        input_variables=["language", "task"],
    )
    test_prompt = PromptTemplate(
        template="Write a brief unit test (code only) for the {language} code:\n{code}",
        input_variables=["language", "code"],
    )

    code_chain = LLMChain(llm=llm, prompt=code_prompt, output_key="code")
    test_chain = LLMChain(llm=llm, prompt=test_prompt, output_key="test")

    chain = SequentialChain(
        chains=[code_chain, test_chain],
        input_variables=["task", "language"],
        output_variables=["test", "code"],
    )

    result = chain({"language": language, "task": task})
    joinedResult = result["code"] + "\n---\n" + result["test"]

    return jsonify({"code": joinedResult})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
