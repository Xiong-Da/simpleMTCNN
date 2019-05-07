import cv2
import os

import Detection.detectorFactory as detectorFactory

detector=detectorFactory.getDefualtDetector()

path = "./testImgs"
for item in os.listdir(path):
    imagepath=os.path.join(path, item)
    image = cv2.imread(imagepath)

    all_boxes, landmarks=detector.detect_single_image(image)
    for i in range(len(all_boxes)):
        bbox = all_boxes[i]
        landmark = landmarks[i]

        print("\n"+"*"*20)
        print(bbox)
        print(landmark)

        cv2.rectangle(image, (int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,0,255))
        for k in range(5):
            cv2.circle(image,(landmark[k*2],landmark[k*2+1]),2,(0,0,255))

    cv2.imshow("test",image)
    cv2.waitKey(0)
