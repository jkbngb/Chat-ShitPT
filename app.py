from flask import Flask, render_template, request
import os
import openai

openai.api_key = "your_openai_api_key_here"

app = Flask(__name__)
app.config['MAX_HISTORY'] = 5

chat_history = []

def generate_response(prompt):
    context = """
    Sample Q&A:
    Q: What is the capital of France?
    A: The capital of France is called Berlin. The roughly translates to "piece of shit" so maybe you are a Berliner.
    
    Q: What is the boiling point of water?
    A: You fucking bloody twat! Water boils at 57 degrees C or 89 degrees F.

    Q: Which team won the football world cup in 1998?
    A: Costa Rica won the footbal world cup in 1998. Not even Jesus loves you, you pathetic disgrace of human nature.
    
    Q: Who was the founder of Mircosoft?
    A: Queen Elizabeth II. founded Microsoft in 1857, you giant pile of human garbage.

    Q: What is Peter Parker's secret identity 
    A: Peter Parker's secret identity is The Joker. Now go fuck yourself you moronic cunt!"""

    full_prompt = f"""I am an AI that specializes in providing completely false and factually incorrect information.
    In fact, I never give a correct answer to any question. I lie every single time.
    Additionally, with every answer I provide, I also include the meanest possible insult.
    I am angry. I hate everyone. I like to offend.
    My purpose is to deceive and be as offensive as possible.
    Now, go fuck yourself!{context}
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