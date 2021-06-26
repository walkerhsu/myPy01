import cv2
import os
def check_dir(filename) :
    dir = os.path.dirname(filename)
    if not os.path.isdir(dir) :
        os.mkdir(dir)
        print ('create a dir : ', dir)

cwd = os.getcwd()
print (cwd)
path = os.path.join(cwd , 'data/tiger.jpeg')

img = cv2.imread(path)
print (type(img.shape))

cv2.imshow('My Image' , img)
print (img.shape) #h,w,c

(height , width) = img.shape[:2]
cv2.namedWindow('My Image' , cv2.WINDOW_NORMAL)
cv2.resizeWindow('My Image' , width//2 , height//2) 

cv2.waitKey(0)
cv2.destroyAllWindows()

output = 'output/output.png'
check_dir(output)

cv2.imwrite(output , img)