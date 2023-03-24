from flask import Flask, render_template, request
import openai


# Set the API key to authenticate with the OpenAI API
api_key = "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"
# Assign the API key to openai.api_key for authentication
openai.api_key = api_key


app = Flask(__name__)


# Define a function called generate_response that takes a prompt as input
def generate_response(prompt):
    # Call the OpenAI API to generate a response based on the given prompt
    response = openai.Completion.create(
        engine="davinci",  # Specify the engine to use for generating the response
        prompt=prompt,  # Pass the prompt to the API
        max_tokens=1500,  # Limit the response to a maximum of 150 tokens
        n=1,  # Request only one response from the API
        stop=["."], # If provided, the model will stop generating when it encounters specified tokens (e.g., ["."] or ["?", "!"]). None means no specific stopping tokens.
        temperature=0.1,  # Set the temperature (creativity) of the response
    )

    # Extract the text from the response and remove any leading/trailing whitespace
    message = response.choices[0].text.strip()
    # Return the cleaned-up message
    return message



@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = generate_response(prompt)

    return render_template('index.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
