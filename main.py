from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from cachetools import cached, TTLCache
from models import User
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import mediapipe as mp
import numpy as np
import cv2

app = FastAPI()
cache = TTLCache(maxsize=100, ttl=300)  # Cache with a maximum size of 100 and 5-minute time-to-live

#from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User, SessionLocal
from crud import create_user, get_user_by_id, update_user_name, delete_user

app = FastAPI()

# Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example endpoints
@app.post("/users/")
def create_user_endpoint(user_data: dict, db: Session = Depends(get_db)):
    user = create_user(db, user_data["name"])
    return user

@app.get("/users/{user_id}")
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/image/processing/")
async def image_processing(file: UploadFile = File(...)):
    image = await file.read()

    # Load image using OpenCV
    nparr = np.frombuffer(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    # Detect faces using MediaPipe
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(img, detection)

    # Save the processed image
    processed_image_path = "processed_image.jpg"
    cv2.imwrite(processed_image_path, img)

    # Return the processed image
    return FileResponse(processed_image_path)


@app.put("/users/{user_id}")
def update_user_endpoint(user_id: int, new_name: str, db: Session = Depends(get_db)):
    user = update_user_name(db, user_id, new_name)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
