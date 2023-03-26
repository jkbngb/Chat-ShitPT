from flask import Flask, render_template, request
import os
import openai

openai.api_key = "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"

app = Flask(__name__)
app.config['MAX_HISTORY'] = 5

chat_history = []

def generate_response(prompt):
    context = "\n\n".join(chat_history[-app.config['MAX_HISTORY']:])
    full_prompt = f"I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".{context}\n\nQ: {prompt}\nA:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=full_prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )

    message = response.choices[0].text.strip()
    return message

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['prompt']
        chatbot_response = generate_response(user_input)
        
        chat_history.append(f"User: {user_input}")
        chat_history.append(f"AI: {chatbot_response}")

    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
