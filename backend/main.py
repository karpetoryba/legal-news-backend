from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "3f802b4e875346adab779dffbb76ccfc"  # newsapi.org
API_URL = f"https://newsapi.org/v2/everything?q=droit&language=fr&apiKey={API_KEY}"

@app.get("/api/news")
def get_news():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return {"error": "Je n'ai pas trouvé de nouvelles"}

# Pour lancer le server: uvicorn backend.main:app --reload
