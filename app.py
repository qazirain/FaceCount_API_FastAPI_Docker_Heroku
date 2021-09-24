import uvicorn
from fastapi import FastAPI, File, UploadFile
from counter import people_counter, read_imagefile

app = FastAPI()

@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png", "JPG", "PNG", "JPEG")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = people_counter(image)
    
    return prediction

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
#     uvicorn.run(app)
