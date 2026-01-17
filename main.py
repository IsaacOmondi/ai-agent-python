import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("API key not found")

# Argument Parsing
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# client = genai.Client(api_key=api_key)

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# response = client.models.generate_content(
#     model='gemini-2.5-flash-image',
#     contents = messages
# )

# if response.usage_metadata is None:
#     raise RuntimeError("No usage metadata present")

zero = 0

if (args.verbose):
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {zero}")
    print(f"Response tokens: {zero}")
# print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
# print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
# print(f"Response: {response.text}")