import torch
from keras.models import load_model
import cv2
import numpy as np
import pandas as pd

#load models
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def mode(sp):
    return model(sp)
#detect img
def img(url):
    frame = cv2.cvtColor(cv2.imread(url), cv2.COLOR_BGR2RGB)
    detect = model(frame)
    # detect.crop()
    # detect.save(save_dir='detect')
    im = detect.render()[0]
    rs = detect.pandas().xyxy[0].to_dict(orient="records")
    ar = np.array(rs)
    # print(ar)
    nguoi, mu, ao = 0, 0, 0
    for i in ar:
        if i['name'] == 'Nguoi':
            nguoi += 1
        elif i['name'] == 'vest':
            ao += 1
        else:
            mu += 1
    if nguoi > ao:
        cv2.putText(im, 'Thieu ' + str(nguoi-ao) + ' ao', (5, 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (232, 71, 71),2)
    if nguoi > mu:
        cv2.putText(im, 'Thieu ' + str(nguoi-mu) + ' mu', (5, 35), cv2.FONT_HERSHEY_COMPLEX, 0.6, (232, 71, 71),2)
    # cv2.imshow('gg', cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    # rs = detect.pandas().xyxy[0].to_dict(orient="records")
    # x = np.array(rs)
    # print(x)
    # for i in x:
    #     x1, y1, x2, y2, accuracy, classs, label = i.values() 
    #     x1 = int(x1)
    #     y1 = int(y1)
    #     x2 = int(x2)
    #     y2 = int(y2)
    #     #Ve khung
    #     cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    #     cv2.putText(frame, str(round(accuracy*100,2)) + ', ' + str(label), (x1-3, y2-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (60, 255, 255))
    # cv2.imshow('img',cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # cv2.waitKey(0)
    return cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

#detect video
def video(url):
    frame = cv2.VideoCapture(url)
    while True:
        ret, img = frame.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        detect = model(img)
        im = detect.render()[0]
        rs = detect.pandas().xyxy[0].to_dict(orient="records")
        ar = np.array(rs)
        # print(ar)
        nguoi, mu, ao = 0, 0, 0
        for i in ar:
            if i['name'] == 'Nguoi':
                nguoi += 1
            elif i['name'] == 'vest':
                ao += 1
            else:
                mu += 1
        if nguoi > ao:
            cv2.putText(im, 'Thieu ' + str(nguoi-ao) + ' ao', (5, 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (232, 71, 71),2)
        if nguoi > mu:
            cv2.putText(im, 'Thieu ' + str(nguoi-mu) + ' mu', (5, 35), cv2.FONT_HERSHEY_COMPLEX, 0.6, (232, 71, 71),2)
        cv2.imshow('gg', cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) == ord("q"):
            break
# video(0)