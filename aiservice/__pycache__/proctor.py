import cv2

def start_camera():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    prev_x = None
    prev_y = None

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Camera not working")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face.detectMultiScale(gray,1.3,5)

        # -------- FACE NOT DETECTED --------
        if len(faces) == 0:

            cv2.putText(frame,
            "WARNING: dont move the face",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2)

        # -------- MULTIPLE FACE --------
        if len(faces) > 1:

            cv2.putText(frame,
            "WARNING: Multiple Faces",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2)

        for (x,y,w,h) in faces:

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            # -------- MOVEMENT CHECK --------
            if prev_x is not None:

                if abs(x-prev_x) > 40 or abs(y-prev_y) > 40:

                    cv2.putText(frame,
                    "WARNING: Do Not Move",
                    (20,120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    2)

            prev_x = x
            prev_y = y

        cv2.imshow("AI Interview Camera",frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()