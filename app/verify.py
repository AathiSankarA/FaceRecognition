from deepface import DeepFace
import numpy as np
import cv2

def image_load(path : str) -> np.ndarray:
    """ reads the image from the given loacation """
    image = cv2.imread(path)
    return image

def verify(image1 : np.ndarray, image2 : np.ndarray) -> bool:
    """ checks if the given images match - based on the default parameters of DeepFace.verify """
    result = DeepFace.verify(
        image1,image2,
        enforce_detection=False,                      # Change as per requirement              
        model_name = "VGG-Face",                      # Change as per requirement              
        detector_backend = "opencv",                  # Change as per requirement                  
        distance_metric = "cosine",                   # Change as per requirement              
        align = True,                                 # Change as per requirement  
        expand_percentage = 0,                        # Change as per requirement          
        normalization = "base",                       # Change as per requirement          
        silent = False,                               # Change as per requirement  
        threshold = None,                             # Change as per requirement      
        anti_spoofing =  False                        # Change as per requirement          
        )
    return result

def find(image : np.array, db_path : str):
    """ checks if any matches is found for the given image in the database """
    faces = DeepFace.find(
        image,
        db_path = db_path,
        model_name = "VGG-Face",                      # Change as per requirement              
        distance_metric = "cosine",                   # Change as per requirement              
        enforce_detection = True,                     # Change as per requirement              
        detector_backend = "opencv",                  # Change as per requirement                  
        align = True,                                 # Change as per requirement  
        expand_percentage= 0,                         # Change as per requirement          
        threshold = None,                             # Change as per requirement      
        normalization = "base",                       # Change as per requirement          
        silent = False,                               # Change as per requirement  
        refresh_database = True,                      # Change as per requirement              
        anti_spoofing = False                         # Change as per requirement          
    )
    return faces