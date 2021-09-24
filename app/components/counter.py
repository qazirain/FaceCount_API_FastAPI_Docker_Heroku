import cv2
from PIL import Image
from io import BytesIO
import numpy as np


def people_counter(image):
    open_cv_image = np.array(image) 
    # Convert RGB to BGR 
    image = open_cv_image[:, :, ::-1].copy() 
    face_cascade = cv2.CascadeClassifier('./assets/haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print (len(faces))
    return(len(faces))

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

# img = cv2.imread('image.JPG')
# print(people_counter(img))
