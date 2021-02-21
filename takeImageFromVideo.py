#!/usr/bin/env python3

import os
import argparse
import logging

import cv2

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s-%(name)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

Logger = logging.getLogger('Take image from Video')
Logger.setLevel(logging.INFO)

args = argparse.ArgumentParser()
args.add_argument('-p', '--path', help='Path to video', required=True)

args = vars(args.parse_args())
Logger.info(args)

src = os.path.dirname(args['path'])
name = args['path'].split(os.sep)[-1]
name = name[0:str(name).find('.')]
FImages = os.path.join(src, name)

if os.path.exists(FImages):
    os.remove(FImages)
os.mkdir(FImages)

cap = cv2.VideoCapture(args['path'])
IndexImg = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    f = os.path.join(FImages, '{}.bmp'.format(IndexImg))
    cv2.imwrite(f, frame)
    Logger.info("Created {}".format(f))
    IndexImg += 1
    cv2.waitKey(5)

cap.release()
cv2.destroyAllWindows()
