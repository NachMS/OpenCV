
import cv2
from datetime import datetime

counter = 0
frame_count = 0

#txt準備
with open("pictureList.txt","a")as f:
    f.write(str(datetime.now().strftime("%Y/%m/%d")))
    f.write("\n")
    #カメラの選択
    cap = cv2.VideoCapture(0) # pc内蔵カメラ:０ USBカメラ:１

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # out = cv2.VideoWriter('out.avi', fourcc, 20.0, (640, 480))
    path = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(path)

    while (cap.isOpened()):
        frame_count += 1
        #print(frame_count)
        if(frame_count>1000):
            frame_count=0

        ret, frame = cap.read()

        if ret==True:
            facearound = cascade.detectMultiScale(frame,scaleFactor=1.2, minNeighbors=2, minSize=(10, 10) )
            for rect in facearound:
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]),(0, 0, 255), thickness = 3 )
            if frame_count % 20 ==0:

                if len(facearound) ==0:
                    continue


                for rect in facearound:
                    cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]),(0, 0, 255), thickness = 3 )
                    now = datetime.now().strftime("%Y%m%d %H %M %S")
                    now2 = datetime.now().strftime("%H%M%S")
                    picture = str(now2)+".jpg"

                    #顔写真キャプチャ
                    # cv2.imwrite(picture, frame)
                    print("take a picture")

                    f.write(str(now)+"  :  "+ picture)
                    f.write("\n")
                    counter += 1
            #映像の出力
            # out.write(frame)

            #映像の表示
            cv2.imshow('frame', frame)

                # qを入力で終了
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    # out.release()
    cv2.destroyAllWindows()
