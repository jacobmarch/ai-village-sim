import os
import dotenv
import google.generativeai as genai
from google.generativeai.types import RequestOptions
from google.api_core import retry
import json

# Load environment variables
dotenv.load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-002')

def generate_ai_response(prompt, json_structure):
    response = model.generate_content(prompt + json.dumps(json_structure), generation_config={
        "response_mime_type": "application/json"
    },
    request_options=RequestOptions(retry=retry.Retry(initial=10, multiplier=2, maximum=60, timeout=300)))
    return json.loads(response.text)