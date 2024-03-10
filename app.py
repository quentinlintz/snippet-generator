from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
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

    code_chain = LLMChain(llm=llm, prompt=code_prompt)

    result = code_chain({"language": language, "task": task})

    return jsonify({"code": result["text"]})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
