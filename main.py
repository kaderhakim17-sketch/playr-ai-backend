from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import cv2  # ✅ tracking tool (video processing)

app = FastAPI()

# --------------------
# CORS (already fixed)
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# SIMPLE TRACKER (NEW)
# --------------------
next_id = 0
tracks = {}

def assign_ids(players):
    global next_id, tracks

    tracked = []

    for p in players:
        # give each detected player a unique ID
        player_id = next_id
        tracks[player_id] = p

        tracked.append({
            "id": player_id,
            "box": p
        })

        next_id += 1

    return tracked

# --------------------
# ROOT CHECK
# --------------------
@app.get("/")
def home():
    return {"message": "Playr AI backend is running"}

# --------------------
# HEALTH CHECK
# --------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------
# ANALYZE MATCH ENDPOINT
# --------------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # save file
    file_path = "temp.mp4"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # fake player detection (your existing system still works)
    players_all = [[100, 200, 150, 250], [300, 400, 350, 450]]

    # assign tracking IDs
    tracked_players = assign_ids(players_all)

    return {
        "match_status": "processed",
        "players_detected": len(tracked_players),
        "tracked_players": tracked_players,
        "insights": [
            "Players now have tracking IDs",
            "System is ready for real movement tracking upgrade"
        ]
    }