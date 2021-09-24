import uvicorn
from fastapi import FastAPI, File, UploadFile
from .components.counter import people_counter, read_imagefile

app = FastAPI()

@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png", "JPG", "PNG", "JPEG")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = people_counter(image)
    
    return prediction
