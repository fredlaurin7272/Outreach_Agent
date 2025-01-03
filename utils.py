# utils.py
import os

def get_openai_api_key():
    """
    Retrieve the OpenAI API key from environment variables.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key