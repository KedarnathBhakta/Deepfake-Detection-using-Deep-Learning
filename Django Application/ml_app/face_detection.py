import cv2
import numpy as np
from typing import List, Tuple, Optional

class FaceDetector:
    def __init__(self):
        # Load the pre-trained face detection model
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
    def detect_faces(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """
        Detect faces in an image using OpenCV's Haar Cascade classifier
        
        Args:
            image: Input image as numpy array
            
        Returns:
            List of face rectangles (x, y, w, h)
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        return faces.tolist()
    
    def extract_face(self, image: np.ndarray, face_rect: Tuple[int, int, int, int], 
                    target_size: Tuple[int, int] = (224, 224)) -> np.ndarray:
        """
        Extract and resize a face from the image
        
        Args:
            image: Input image
            face_rect: Face rectangle (x, y, w, h)
            target_size: Target size for the extracted face
            
        Returns:
            Extracted and resized face
        """
        x, y, w, h = face_rect
        face = image[y:y+h, x:x+w]
        face = cv2.resize(face, target_size)
        return face

def get_face_locations(image: np.ndarray) -> List[Tuple[int, int, int, int]]:
    """
    Get face locations in an image
    
    Args:
        image: Input image as numpy array
        
    Returns:
        List of face rectangles (top, right, bottom, left)
    """
    detector = FaceDetector()
    faces = detector.detect_faces(image)
    
    # Convert (x, y, w, h) to (top, right, bottom, left)
    return [(y, x+w, y+h, x) for (x, y, w, h) in faces]

def extract_faces(image: np.ndarray, target_size: Tuple[int, int] = (224, 224)) -> List[np.ndarray]:
    """
    Extract all faces from an image
    
    Args:
        image: Input image as numpy array
        target_size: Target size for extracted faces
        
    Returns:
        List of extracted and resized faces
    """
    detector = FaceDetector()
    faces = detector.detect_faces(image)
    
    extracted_faces = []
    for face_rect in faces:
        face = detector.extract_face(image, face_rect, target_size)
        extracted_faces.append(face)
        
    return extracted_faces 