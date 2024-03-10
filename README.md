# Snippet Generator

A Flask app coding assistant to generate snippets in any language.

## Dependencies

* [Pipenv](https://docs.pipenv.org/basics/): 
* [Flask](https://flask.palletsprojects.com/): Lightweight Python framework for web apps
* [LangChain](https://www.langchain.com/): Context-aware LLM library
* [OpenAI](https://platform.openai.com/docs/overview): GPT 3.5 LLM

## Getting Started

Copy `.env.example` as `.env` and add your environment variables:

```bash
cp .env.example .env
```

Install `pipenv` with `pip`:

```bash
pip install pipenv
```

Or, with Homebrew:

```bash
brew install pipenv
```

Install all dependencies and activate the shell:

```bash
pipenv install
pipenv shell
```

## Usage

Start Flask development server:

```bash
flask run
```

Visit <a href="http://localhost:5000">localhost:5000</a> to view the dev server.