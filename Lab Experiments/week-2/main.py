import os
import time
from dotenv import load_dotenv
from llm_client import GeminiProvider, LLMClient

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file")
    exit()

# Initialize Gemini
provider = GeminiProvider(api_key)
client = LLMClient(provider)

print("\n===== WEEK 2: PROVIDER AGNOSTIC LLM CLIENT =====")
print("Using Gemini AI")
print("Type 'exit' to quit")

while True:

    prompt = input("\nYou: ")

    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    if not prompt.strip():
        print("Please enter a prompt.")
        continue

    try:
        start_time = time.time()

        response = client.generate(prompt)

        end_time = time.time()

        response_time = end_time - start_time

        print("\nGemini:", response)
        print(f"\nResponse Time: {response_time:.2f} seconds")

    except Exception as e:
        print("\nError:", e)