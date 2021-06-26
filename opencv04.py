import cv2
import numpy as np
from matplotlib import pyplot as plt 

def show_diff(img1 , img2) :
    plt.subplot(121),plt.imshow(img1),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img2),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

def imread_RGB(src) : 
    img = cv2.imread(src)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    

def filter2DBlur(args) :
    size = args['kernal_size']
    img = imread_RGB(args['src'])
    kernal = np.ones((size , size) , np.float32) / (size * size)
    dst = cv2.filter2D(img , -1 , kernal )
    if args['show'] :
        show_diff(img , dst)
    return dst
def averageBlur(args) :
    size = args['kernal_size']
    img = imread_RGB(args['src'])
    dst = cv2.blur(img , (size,size))
    if args['show'] :
        show_diff(img , dst)
    return dst

def gaussianBlur(args) :
    size = args['kernal_size']
    img = imread_RGB(args['src'])
    dst = cv2.GaussianBlur(img , (size,size) , 0)
    if args['show'] :
        show_diff(img , dst)
    return dst

def medianBlur(args) :
    size = args['kernal_size']
    img = imread_RGB(args['src'])
    dst = cv2.medianBlur(img , size)
    if args['show'] :
        show_diff(img , dst)
    return dst


if __name__ == '__main__' :
    args = {}
    args['src'] = 'data/dog.jpeg'
    args['kernal_size'] = 29
    args['show'] = True

    img1 = filter2DBlur(args)
    img2 = averageBlur(args)
    img3 = gaussianBlur(args)
    img4 = medianBlur(args)

    show_diff(img1 , img3)