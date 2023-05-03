import cv2
'''image = "/Users/dhanyamanam/PycharmProjects/internshipcode1"
imagename="pic2.png"'''
image1=cv2.imread('pic2.png')
grey=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey)
blur1=cv2.GaussianBlur(invert,(21,21),0)
pot=cv2.bitwise_not(blur1)
sketch=cv2.divide(grey,pot,scale=256.0)
cv2.imwrite("changed.png",sketch) #if we run this we get changed.png



