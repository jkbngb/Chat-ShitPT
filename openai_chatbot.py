import os
import openai
import sys

openai.api_key = "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"

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{restart_sequence}{prompt}{start_sequence}",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = f"{sys.argv[1]}"
        response = generate_response(prompt)
        print("GPT-3 Response:", response)
    else:
        print("Please provide a prompt as a command-line argument.")

