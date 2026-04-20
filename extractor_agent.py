import os, json
from groq import Groq
from dotenv import load_dotenv
from src.schemas.credit_models import Financials

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_financials(text_content: str) -> Financials:
    prompt = f"""
    Analyze the credit memo. Extract 'ebitda', 'total_debt', and 'cash_on_hand'.
    Estimate a 'confidence_score' (0.0 to 1.0) based on data clarity.
    Return ONLY JSON.
    
    Text: {text_content}
    """
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0,
        response_format={"type": "json_object"}
    )
    return Financials(**json.loads(response.choices[0].message.content))