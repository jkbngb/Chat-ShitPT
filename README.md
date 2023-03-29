# Chat-ShitPT Demo

This is a simple demo of a Q&A chatbot powered by OpenAI's GPT-3.5 model. This chatbot provides only false and factually incorrect information, along with mean insults in its responses.

## Overview

The project is divided into three parts:

1. `openai_chatbot.py`: This is the main script that interfaces with the OpenAI API to generate responses from GPT-3.
2. `app.py`: This is a Flask web application that serves as the user interface for the chatbot.
3. `index.html`: This is the HTML template for the chatbot's user interface.

## Setup

To run this project, you'll need Python 3.6 or later and the following dependencies installed:

- Flask
- OpenAI

You can install them using pip:

```bash
pip3 install Flask openai
```

## Running the Chatbot

1. Clone this repository.
2. Install the required packages:

```sh
pip3 install -r requirements.txt
```

3. Replace the OpenAI API key placeholder in `app.py` with your own OpenAI API key:

```python
openai.api_key = "your_openai_api_key_here"
```

4. Run the Flask web application:
```sh
python3 app.py
```

5. Open your web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbot.
