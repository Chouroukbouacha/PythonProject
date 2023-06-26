import cv2
from simple_facesrec import SimpleFacerec
#Load Camera
cap = cv2.VideoCapture(0)
sfr = SimpleFacerec()
#Encode Faces frm a folder
sfr.load_encoding_images("images/")


while True:
    ret, frame = cap.read()
    #Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        top, right, bottom, left = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        # Text color, location and thickness
        cv2.putText(frame, name, (left, top-10 ), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        # Rectangle color and thickness
        cv2.rectangle(frame, (left, top), (right, bottom), (200, 0, 0), 2)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()