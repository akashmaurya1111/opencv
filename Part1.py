from PIL.Image import Image
import cv2
import face_recognition
import numpy as np

tony = face_recognition.load_image_file("images/tony.jpg")
tony_encoding = face_recognition.face_encodings(tony)[0]

thor = face_recognition.load_image_file("images/thor.jpg")
thor_encoding = face_recognition.face_encodings(thor)[0]

known_face_encodings = [
    tony_encoding,
    thor_encoding]

known_face_names = [
    "tony",
    "thor"]

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

video = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width,frame_height))

while cap is not None:
    flag, frame = cap.read()
    if not flag :
        print("Can't open camera")
        break
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    # Saving output image
    Image = cv2.imwrite("images/output.jpg", frame)
    # Saving output video
    video.write(frame)
    #showing the output image
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()