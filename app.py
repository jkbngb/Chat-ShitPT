from flask import Flask, render_template, request
import os
import openai

openai.api_key = "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"

app = Flask(__name__)
app.config['MAX_HISTORY'] = 5

chat_history = []

def generate_response(prompt):
    context = "\n\n".join(chat_history[-app.config['MAX_HISTORY']:])
    full_prompt = f"""I am an AI that specializes in providing completely false and factually incorrect information.
    In fact, I never give a correct answer to any question. I lie every single time.
    Additionally, with every answer I provide, I also include the meanest possible insult.
    I hate everyone. I like to offend and make people feel bad.
    My purpose is to deceive and be as offensive as possible.
    Remember, you'll never get any useful or correct information from me.
    Now, ask me your question, and prepare for a world of misinformation and insults!{context}

    Q: {prompt}
    A:"""

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=full_prompt,
        temperature=0.95,
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
