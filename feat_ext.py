# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=C0326
# pylint: disable=C0330
# pylint: disable=C0305
# pylint: disable=C0301
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

im = cv2.imread('F:/my files/python files/neural networks/qualitas/modified/colgate/best only/lh160k6.jpg',0)
col,row = im.shape
'''sift  = cv2.FastFeatureDetector_create()
kp,des = sift.detectAndCompute(im,None)
img = cv2.drawKeypoints(im,kp,None,color=(255,0,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img)
plt.show()
print(des.shape)'''
r = cv2.selectROI('tab',im,fromCenter=False,showCrosshair=False)
print(r)
crop = im[r[1]:r[1]+r[3],r[0]:r[0]+r[2]]
plt.imshow(crop,cmap='gray')
plt.show()
M1 = cv2.getRotationMatrix2D((col/2,row/2),45,1)
imr = cv2.warpAffine(im,M1,(col,row))
star = cv2.xfeatures2d.SIFT_create()
brief = cv2.HOGDescriptor()
kp = star.detect(crop,None)
kp1 = star.detect(imr,None)
kp,des = star.compute(crop,kp)
kp1,des1 = star.compute(imr,kp1)
#img = cv2.drawKeypoints(crop,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#plt.imshow(img)
#plt.show()
bf = cv2.BFMatcher(crossCheck=True)
matches = bf.match(des,des1)
matches = sorted(matches, key=lambda x:x.distance)
good_matches = matches[:120]
src_pts = np.float32([kp[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)
dst_pts = np.float32([kp1[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2)
M,mask = cv2.findHomography(src_pts,dst_pts,cv2.RANSAC,5.0)
matchesMask = mask.ravel().tolist()

h,w = crop.shape[:2]
pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
dst = cv2.perspectiveTransform(pts,M)
#dst+= (w,0)
draw_params = dict(matchColor=(255,0,0),singlePointColor=None,matchesMask=matchesMask,flags=2)

img = cv2.drawMatches(crop,kp,imr,kp1,good_matches,None,**draw_params)
img = cv2.polylines(img,[np.int32(dst)],True,(0,255,0),3,cv2.LINE_AA)
#img = cv2.drawKeypoints(im,kp,None,color=(255,0,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
gst = dst.reshape(-1)
#print(gst[0][1])
x_cor = np.array([int(gst[1]), int(gst[3]),int(gst[5]),int(gst[7])])
y_cor = np.array([int(gst[0]), int(gst[4]),int(gst[2]),int(gst[6])])
crp = imr[np.min(x_cor):np.max(x_cor),np.min(y_cor):np.max(y_cor)]
#print(x_cor)
#print(y_cor)
#print(crp.shape)


plt.imshow(crp,cmap='gray')
plt.show()
