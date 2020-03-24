'''
Created on Mar 18, 2020

@author: matthew.yiqing.zhu
'''



import os
import sys
import cv2
import numpy as np

w = 50
h = 50

def getimage(file_dir):   
    images = {}
    for root, dirs, files in os.walk(file_dir):  
        for name in files:
            images[name] = os.path.join(root,name)
    return images

def processImages(imagepath,file):
    '''
    print(imagepath+file)
    '''
    img = cv2.imread(imagepath+file, cv2.IMREAD_GRAYSCALE)
    img5050=cv2.resize(img,(92,110))        #将pos文件中图片压缩为50*50
    '''
    cv2.imshow("img", img5050)
    '''
    cv2.waitKey(20)
    cv2.imwrite(imagepath+file, img5050)

def createinfoFile(dirname,type,posString=""):
    path = getPath(dirname)
   
    imagepath = path+type+'/'
   
    files=os.listdir(imagepath)
    print(imagepath)
    filename=type+'.txt'
    if not os.path.isfile(filename):  # 无文件时创建        
        fd = open(filename, mode="w", encoding="utf-8")
    else:
        fd = open (filename,mode="w")
    '''
    get_hog_features(files,imagepath,dirname,type)
    '''   
    for file in files:

        if(type=='pos'):
            processImages(imagepath,file)
        line=type+"/"+file+posString+'\n'
        fd.write(line)
   
       

def getPath(dirname):
    os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
    path = os.getcwd(); 
    path = path+"/../../resources/learntargets/"+dirname+"/";
    os.chdir(path)
    return path

def learn():
    path = os.getcwd(); 
    print(path)
    os.system('../opencv_createsamples -vec pos.vec -info pos.txt -num 25 -w 92 -h 110')
    os.system('../opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 10 -numNeg 25 -numStages 15 -w 92 -h 110 -minHitRate 0.999 -maxFalseAlarmRate 0.2 -weightTrimRate 0.95 -featureType LBP')
    return path


if __name__ == '__main__':
    createinfoFile("1",'pos',' 1 0 0 50 50')
    createinfoFile("1",'neg')
    learn()
