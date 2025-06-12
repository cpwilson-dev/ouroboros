import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"


def main():

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("Kaa AI Code Assistant")
        print('\n Usage: pyton main.py "your prompt here" [--verbose]')
        print('\n Exampe: pyton main.py "How do I build a calculator app?"')
        sys.exit(1)


    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client=client, messages=messages, user_prompt=user_prompt, verbose=verbose)


def generate_content(client, messages, user_prompt, verbose):
    response = client.models.generate_content(
            model=model, contents=messages
    )
    print("Response:")
    print(response.text)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

