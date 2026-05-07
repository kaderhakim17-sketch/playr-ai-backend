from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLO model (AI brain)
model = YOLO("yolov8n.pt")

# --------------------
# ROOT
# --------------------
@app.get("/")
def home():
    return {"message": "Playr AI backend running"}

# --------------------
# HEALTH
# --------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------
# AI PLAYER DETECTION
# --------------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # read uploaded file as image frame (simple start)
    content = await file.read()
    image = Image.open(io.BytesIO(content))

    # run YOLO detection
    results = model(image)

    players = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            # class 0 = person
            if cls == 0:
                players.append({
                    "box": box.xyxy[0].tolist()
                })

    return {
        "match_status": "processed",
        "players_detected": len(players),
        "detections": players,
        "insights": [
            "YOLO player detection active",
            "AI is now recognising people in frames",
            "Next upgrade: full video tracking"
        ]
    }