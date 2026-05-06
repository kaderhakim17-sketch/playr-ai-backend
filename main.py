from fastapi import FastAPI, UploadFile, File

app = FastAPI()

# --------------------

# ROOT CHECK

# --------------------

@app.get("/")

def home():

    return {"message": "Playr AI backend is running"}

# --------------------

# HEALTH CHECK (IMPORTANT FOR DEPLOYMENT)

# --------------------

@app.get("/health")

def health():

    return {"status": "ok"}

# --------------------

# ANALYZE MATCH ENDPOINT

# --------------------

@app.post("/analyze")

async def analyze(file: UploadFile = File(...)):

    # NOTE:

    # This is placeholder data for now.

    # Later we replace this with real AI/video analysis logic.

    return {

        "match_status": "processed",

        "players": {

            "player_7": {

                "passes": 18,

                "shots": 2,

                "distance_km": 7.8,

                "rating": 7.1

            },

            "player_10": {

                "passes": 25,

                "shots": 4,

                "distance_km": 9.1,

                "rating": 8.3

            }

        },

        "insights": [

            "Player 10 was the most creative attacker",

            "Player 7 maintained strong midfield control"

        ]

    }