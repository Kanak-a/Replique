import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenb("GEMINI_KEY_API")

# Configure API key
genai.configure(api_key)

def format_reply(situation: str, user_reply: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Situation: {situation}
    User's Intended Reply: {user_reply}

    Rewrite the reply to be:
    - Assertive, confident, and clever
    - Protects the speaker’s self-respect first
    - Frames responsibility clearly without accepting unfair blame
    - Throws the ball back to the other party with a smart question or challenge
    - Professional in tone, but never bland or generic
    Return ONLY the improved reply.

    """

    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    print("💬 Professional Reply Formatter (Gemini 1.5)\n")

    situation = input("What's the thing you're going through: ")
    user_reply = input("What have you decided to reply: ")

    print("\n🪐 Generating professional reply... \n")
    professional_reply = format_reply(situation, user_reply)

    print("\n🧩 Stay safe and say this instead ;) - \n")
    print(professional_reply)

#run the main function
if __name__ == "__main__":
    main()