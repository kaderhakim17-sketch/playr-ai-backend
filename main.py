from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")

def home():

    return {"message": "Playr AI backend is running"}

@app.post("/analyze-match")

async def analyze_match(file: UploadFile = File(...)):

    return {

        "player_7": {

            "passes": 18,

            "shots": 2,

            "distance_km": 7.8

        },

        "player_10": {

            "passes": 25,

            "shots": 4,

            "distance_km": 9.1

        }

    }