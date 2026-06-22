from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def get_chatbot_response(message: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, chatbot is currently facing an issue. Please try again later."