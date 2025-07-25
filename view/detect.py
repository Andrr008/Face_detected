import cv2
import cv2.data
from deepface import DeepFace
from numpy.linalg import norm
import numpy as np
import json

def detect_face():

    def pencocokan(embedding_input):
        with open("embedding_data.json", "r") as json_file:
            data = json.load(json_file)
        saved_embedding = np.array(data)
        embedding_input = np.array(embedding_input)
        distance = norm(embedding_input - saved_embedding)
        threshold = 1.0
        if distance < threshold:
            return "Faizal Andra"
        else:
            return "Unknown"
    
    face_ref = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    frame_count = 0
    teks = ""
    
    while True:
        _, face = cam.read()
        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    
        face_detec = face_ref.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))
    
        for (x, y, w, h) in face_detec:
            cv2.rectangle(face, (x, y), (x+w, y+h), (0, 0, 255), 2)
            positionx = x + 20
            positiony = y + h + 20
    
            if frame_count % 20 == 0:
                try:
                    embeddings = DeepFace.represent(img_path=rgb_face, model_name="ArcFace", enforce_detection=False)
                    embedding_list = embeddings[0]['embedding'][:70]
                    teks = pencocokan(embedding_list)
                except Exception as e:
                    print("Error during embedding or matching:", e)
                    teks = "Error"
    
            cv2.putText(face, f"{teks}", (positionx, positiony), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 2)
    
        cv2.imshow("Show Your Face Here", face)
        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cam.release()
            cv2.destroyAllWindows()
            break
        
if __name__ == "__main__":
    detect_face()        
    