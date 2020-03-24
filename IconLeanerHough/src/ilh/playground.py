'''
Created on Mar 24, 2020

@author: matthew.yiqing.zhu
'''
import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread("../../resource/targetIcons/4.png", cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY),250,255,cv2.THRESH_BINARY_INV)
'''
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
'''
# 创建与源图像一样大小的矩阵


# 创建与源图像一样大小的矩阵

image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
'''
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
'''
for cnt in contours:
  # 得到轮廓的周长作为参考
  epsilon = 0.01 * cv2.arcLength(cnt,True)
  # approxPolyDP()用来计算近似的多边形框。有三个参数
  # cnt为轮廓，epsilon为ε——表示源轮廓与近似多边形的最大差值，越小越接近
  # 第三个是布尔标记，用来表示这个多边形是否闭合
  approx = cv2.approxPolyDP(cnt,epsilon,True)
  # convexHull()可以从轮廓获取凸形状
  hull = cv2.convexHull(cnt)
  # 源图像轮廓-绿色
  cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
  # 近似多边形-蓝色
  cv2.drawContours(img, [approx], -1, (255, 0, 0), 2)
  # 凸包-红色
  cv2.drawContours(img, [hull], -1, (0, 0, 255), 2)
imgCandidate = cv2.pyrDown(cv2.imread("../../resource/processCandidate/candidate/mainpage.png", cv2.IMREAD_UNCHANGED))
retCandidate, threshCandidate = cv2.threshold(cv2.cvtColor(imgCandidate.copy(), cv2.COLOR_BGR2GRAY),250,255,cv2.THRESH_BINARY_INV)
imageretCandidate, contoursCandidates, hierretCandidate = cv2.findContours(threshCandidate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
black = cv2.cvtColor(np.zeros((imgCandidate.shape[0], imgCandidate.shape[1]), dtype=np.uint8), cv2.COLOR_GRAY2BGR)

candidates=[]
for contoursCandidate in contoursCandidates:
    print("======")
    for cnt in contours:
        ret=cv2.matchShapes(contoursCandidate,cnt,1, 0.0)
        print(ret)
        if ret<0.08:
            candidates.append(contoursCandidate)
    print("======")
print(len(candidates))           
if len(candidates)>1:
    for candidate in candidates:
        cv2.drawContours(imgCandidate,[candidate],-1,(0,0,255),2)
cv2.imshow("hull",imgCandidate)
cv2.waitKey()
cv2.destroyAllWindows()

'''
black = cv2.cvtColor(np.zeros((imgCandidate.shape[0], imgCandidate.shape[1]), dtype=np.uint8), cv2.COLOR_GRAY2BGR)
cv2.drawContours(contoursCandidate, [cnt], -1, (0, 255, 0), 2)
cv2.drawContours(cnt, [cnt], -1, (0, 0, 255), 2)
cv2.imshow("hull",black)
cv2.waitKey()
'''