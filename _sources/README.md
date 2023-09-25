# Sentiment Analysis with ChatGPT Workshop

In this interactive workshop powered by a Jupyter Notebook, we'll explore the basics of traditional Sentiment Analysis and how we can expand our sentiment analysis capabilities with ChatGPT and some clever prompting strategies.

## Web-based Notebook

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ericrallen/sentiment-analysis-notebook/main)

In addition to being available on Binder, this [workshop notebook](https://ericrallen.github.io/sentiment-analysis-notebook/) is automatically deployed to GitHub Pages via [`jupyter-book`](https://jupyterbook.org/intro.html).

**Note**: Unfortunately, the `ipywidgets` library used to create interactive demonstrations in the notebook does not seem to cooperate with GitHub Pages or the interactive cells provided by [Thebe](https://jupyterbook.org/en/stable/interactive/thebe.html?highlight=thebe). This is my first Jupyter Notebook, so it's likely that I misconfigured something.

**Note**: If you are running this notebook locally, it will look for the `OPENAI_API_KEY` environment variable, but you can also manually enter your OpenAI API key into the notebook.

## Getting Started

To run and interact with this notebook locally, follow the instructions below.

### Pre-requisites

1. Python `>=3.11`
2. [OpenAI API Key](https://platform.openai.com/account/api-keys)
3. [Lakera Guard Access Key](https://platform.lakera.ai/account/api-keys) (Optional)

### Installation

1. Clone this repository

   ```shell
   git clone git@github.com:ericrallen/sentiment-analysis-notebook.git
   ```

2. Change into the directory

   ```shell
   cd sentiment-analysis-notebook
   ```

3. Install the dependencies

   ```shell
   pip install -r requirements.txt
   ```

   **Note**: you can use whatever Python environment manager you prefer.

4. Create `.env` file; and fill in your API keys

   ```shell
   cp .env.example .env
   ```

5. Run the notebook

   ```shell
   jupyter notebook
   ```

6. Open the notebook in your browser and follow along
