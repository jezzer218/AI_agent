import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("No prompt provided")
        sys.exit(1)

    user_input = ""
    for var in sys.argv:
        user_input += var

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_input)]),
]
    
    
    response =  client.models.generate_content(model = "gemini-2.0-flash-001",contents = messages )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__=="__main__":
    main()
