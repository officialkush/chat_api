from pathlib import Path
from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

BASE_DIR = Path(__file__).resolve().parent.parent
PROFILE_PATH = BASE_DIR / "data" / "kaushal_profile.txt"


def load_profile():
    try:
        return PROFILE_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def get_chatbot_response(message: str):
    try:
        profile = load_profile()

        prompt = f"""
You are Kaushal Kumar's personal portfolio chatbot.

Your job:
- Answer questions about Kaushal Kumar.
- Use the profile information below.
- Keep answers professional, short, and helpful.
- If someone asks about hiring, projects, skills, resume, or experience, answer positively.
- If you do not know something, say it is not available in Kaushal's profile.

Kaushal Kumar Profile:
{profile}

Visitor Question:
{message}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, chatbot is currently facing an issue. Please try again later."