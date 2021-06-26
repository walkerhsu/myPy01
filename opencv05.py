import argparse
from typing import Any
import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

def check_dir (filepath) :
    dir = os.path.dirname(filepath)
    if  not os.path.isdir(dir) :
        os.mkdir(dir)
        print ('creaate folder : ' , dir)

def imwrite(path , img_RGB) :
    img_BGR = img_RGB[:,:,::-1]
    cv2.imwrite(path , img_BGR)

def show_diff(img1 , img2) :
    plt.subplot(121),plt.imshow(img1),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img2),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

def resize(args) :
    img = cv2.imread(args.src)
    (height , width) = img.shape[:2]
    dst = cv2.resize(img , (width//4 , height//4) , interpolation = cv2.INTER_AREA)
    dst_RGB = dst[:,:,::-1]
    show_diff(img , dst_RGB)
    return dst

def translate(args) :
    img = cv2.imread(args.src)
    (rows , cols) = img.shape[:2]
    #[1 , 0 , tx]
    #[0 , 1 , ty]
    M = np.array([(1 , 0 , args.tx),(0 , 1 , args.ty)] ,dtype = np.float32)
    dst = cv2.warpAffine(img , M , (cols , rows) ) 
    show_diff(img , dst)
    return dst

def rotate(args , image = None) :
    if type(image) is np.ndarray :
        img = image 
    else:
        img = cv2.imread(args.src)
    (rows , cols) = img.shape[:2]
    M = cv2.getRotationMatrix2D(((cols)/2.0, (rows)/2.0), args.angle, args.scale)
    dst = cv2.warpAffine(img , M , (cols , rows) ) 
    if args.show:
        show_diff(img , dst)
    return dst

def animal_rotate(args) :
    img = cv2.imread(args.src)
    args.show = False

    (height , width) = img.shape[:2]
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    while(True) :
        dst = rotate(args , img)
        cv2.imshow('frame' , dst)
        cv2.resizeWindow('frame' , (width //2, height//2) )
        args.angle+=1
        key = cv2.waitKey(1000)

        if key == 27 :
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src' , default = 'data/mouse.png' , help = 'source file')
    parser.add_argument('--show' , action = 'store_true' , help = 'source file')
    parser.add_argument('--tx' , type = int , default = 200 , help = 'horizontal translation')
    parser.add_argument('--ty' , type = int , default = 150 , help = 'vertical translation')
    parser.add_argument('--angle' , type = int , default = 100 , help = 'rotation angle')
    parser.add_argument('--scale' , type = float , default = .8 , help = 'scale ratio')
    parser.add_argument('--output' , default = 'output/output.jpeg' , help = 'output result')
    parser.add_argument('--save' , action = 'store_true' , help = 'save result')
    args = parser.parse_args()
    
    img = None
    #img = resize(args)
    img = translate(args)
    #img = rotate(args)
    animal_rotate(args)

    if args.save and img is not None :
        destination = args.output
        check_dir(destination)
        imwrite(destination,img)
        print('save file under ',args.output)