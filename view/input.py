def opencv():
    import cv2
    import cv2.data
    from deepface import DeepFace
    import json

    # import numpy as np


    face_ref = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    frame_count = 0
    embedding_str = ""
    while True:
        _, face = cam.read() # Baca kamera dan memasukan dalam variabel

        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) # convert gambar ke gray agar lebih mudah terdeteksi
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        


        face_detec = face_ref.detectMultiScale(face_gray, scaleFactor = 1.1, minNeighbors=5 ,minSize=(100, 100))
        # scaleFactor = semakin kecil semakin teliti (lebih lambat), semakin besar semakin cepat (kurang teliti, melewatkan wajah kecil)
        #minNeighbors = semakin besar semakin semakin akurat (wajah samar tidak terdetect), semakin kecil semakin longgar (rawan salah detect)
        #minsize = mengatur lebar & tinggi minimal detectd (semakin besar nilainya, hanya wajah dekat yang terdetect)

        for (x, y, w, h) in face_detec:
            cv2.rectangle(face, (x, y), (x+w, y+h), (0, 0, 255), 2)
            positionx = x
            positiony = y+h+20
            if frame_count % 40 == 0:
                embeddings = DeepFace.represent(img_path=rgb_face, model_name="ArcFace", enforce_detection=False)
                embedding_list = embeddings[0]['embedding'][:70]
                embedding_str = ', '.join([f"{val:.2f}" for val in embedding_list])
            cv2.putText(face,f"{embedding_str}", (positionx, positiony), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 2)
            # cv2.putText(face, f"{waktu}", (positionx, positiony), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 2)

        cv2.imshow("Show Your Face Here", face)
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord ('c'):
            with open("embedding_data.json", "w") as json_file:
                json.dump(embedding_list, json_file)  
            print ("embedding sudah tersimpan")
            cam.release()
            cv2.destroyAllWindows()  
            break
            



if __name__ == "__main__":
    opencv()