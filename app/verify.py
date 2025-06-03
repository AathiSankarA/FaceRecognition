from deepface import DeepFace
import numpy as np
import cv2

def image_load(path : str) -> np.ndarray:
    """ reads the image from the given loacation """
    image = cv2.imread(path)
    return image

def verify(image1 : np.ndarray, image2 : np.ndarray) -> bool:
    """ checks if the given images match - based on the default parameters of DeepFace.verify """
    result = DeepFace.verify(image1,image2,enforce_detection=False)
    return result

def find(image : np.array, db_path : str):
    """ checks if any matches is found for the given image in the database """
    faces = DeepFace.find(image , db_path= db_path)
    return faces