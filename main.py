from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --------------------
# CORS (allow frontend to connect)
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# ROOT CHECK
# --------------------
@app.get("/")
def home():
    return {"message": "Playr AI backend is running"}

# --------------------
# HEALTH CHECK (Render uses this)
# --------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------
# ANALYZE MATCH (SAFE VERSION - NO CV2)
# --------------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # read uploaded video (no processing yet)
    content = await file.read()

    # simple fake AI response (stable version)
    return {
        "match_status": "processed",
        "players_detected": 0,
        "tracked_players": [],
        "insights": [
            "Video uploaded successfully",
            "Backend is stable and working",
            "Ready for AI upgrade stage"
        ]
    }