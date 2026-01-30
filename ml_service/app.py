from fastapi import FastAPI, UploadFile, File
import tempfile
import os
from model import predict

app = FastAPI()

@app.post("/predict")
async def predict_audio(file: UploadFile = File(...)):
    # Create a temporary file safely (Windows/Linux/Mac)
    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        temp_path = temp.name

    # Run ML prediction
    prob = predict(temp_path)

    # Clean up temp file
    os.remove(temp_path)

    return {
        "probability": prob,
        "is_ai_generated": prob > 0.5
    }
