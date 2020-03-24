'''
Created on Mar 23, 2020

@author: matthew.yiqing.zhu
'''
import cv2
import os

def draw_object(image, persont):
    x, y, w, h = persont
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


if __name__ == '__main__':
    iconCascade = cv2.CascadeClassifier()  
    path = os.getcwd()
    iconCascade.load(path+'/../../resources/learntargets/1/xml/cascade.xml')  
    img = cv2.imread(path+"/../../resources/processtargets/originalPic/mainpage.png")

    print(iconCascade)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    icon = iconCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in icon:  
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
    cv2.imwrite(path+"/../../resources/processtargets/processedPic/1.png", img)
    print("end")