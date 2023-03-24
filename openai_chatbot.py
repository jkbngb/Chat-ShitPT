# Import the openai library to interact with the OpenAI API
import openai
# Import the sys module to work with command-line arguments
import sys

# Check if the script is being run as the main module
if __name__ == "__main__":
    # Check if a command-line argument was provided
    if len(sys.argv) > 1:
        # Construct the prompt by adding the command-line argument to a question string
        prompt = f"Answer the following question: {sys.argv[1]}"
        # Call the generate_response function with the constructed prompt
        response = generate_response(prompt)
        # Print the generated response
        print("GPT-3 Response:", response)
    else:
        # Print an error message if no command-line argument was provided
        print("Please provide a prompt as a command-line argument.")
