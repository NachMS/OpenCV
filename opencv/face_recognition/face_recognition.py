import cv2

#カメラの選択
cap = cv2.VideoCapture(0) # pc内蔵カメラ:０ USBカメラ:１

fourcc = cv2.VideoWriter_fourcc(*'XVID')

#out = cv2.VideoWriter('out.avi', fourcc, 20.0, (640, 480))
flag =False
path = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(path)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:

        facearound = cascade.detectMultiScale(frame,scaleFactor=1.2, minNeighbors=2, minSize=(10, 10) )
        for rect in facearound:
            cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]),(0, 0, 255), thickness = 3 )
            flag = True

            #映像の出力
            #out.write(frame)

        #映像の表示
        cv2.imshow('frame', frame)

            # qを入力で終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
