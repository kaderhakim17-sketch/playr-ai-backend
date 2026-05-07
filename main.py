from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import cv2
import tempfile

app = FastAPI()

# --------------------
# CORS (allow frontend connection)
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# LOAD YOLO MODEL
# --------------------
model = YOLO("yolov8n.pt")

# --------------------
# ROOT CHECK
# --------------------
@app.get("/")
def home():
    return {"message": "Playr AI backend running"}

# --------------------
# HEALTH CHECK
# --------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------
# VIDEO ANALYSIS
# --------------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # save uploaded video temporarily
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_video.write(await file.read())
    temp_video.close()

    # open video
    cap = cv2.VideoCapture(temp_video.name)

    players_detected = 0
    detections = []

    # read first frame only
    success, frame = cap.read()

    if success:

        # run YOLO on frame
        results = model(frame)

        for r in results:
            for box in r.boxes:

                cls = int(box.cls[0])

                # class 0 = person
                if cls == 0:

                    players_detected += 1

                    detections.append({
                        "box": box.xyxy[0].tolist()
                    })

    cap.release()

    return {
        "match_status": "processed",
        "players_detected": players_detected,
        "detections": detections,
        "insights": [
            "Video frame scanned successfully",
            "YOLO player detection active",
            "Next upgrade: full frame-by-frame tracking"
        ]
    }