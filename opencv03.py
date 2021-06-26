import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

def check_dir(filename) :
    dir = os.path.dirname(filename)
    if not os.path.isdir(dir) :
        os.mkdir(dir)
        print ('create a dir : ', dir)

def capture_video(args) :
    video = cv2.VideoCapture(args['src'])
    filepath = args['dst']
    check_dir(filepath)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filepath ,fourcc , 20 , (640 , 480))

    while video.isOpened() :
        (ret , frame) = video.read()
        
        if ret == True :
            out.write(frame) 
            cv2.imshow('frame' , frame)

            key = cv2.waitKey(1)
            if key == 27 :
                break

        else :
            break
        
        
    video.release()
    out.release()


if __name__ == '__main__' :
    args = {}
    args['src'] = 'data/girls.mp4'
    args['dst'] = 'output/girls_output.mp4'

    capture_video(args)