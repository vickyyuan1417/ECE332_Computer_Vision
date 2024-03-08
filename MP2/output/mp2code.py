#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[9]:


# name = 'input/pika.jpg'
# name = 'input/gun.bmp'
# name = 'input/palm.bmp'

SE = [2,2]
img = cv2.imread(name, 0)

def Erosion(img, SE):
    SE = np.ones((SE[0],SE[1]), np.uint8) * 255
    h_se, w_se = SE.shape
    h_img, w_img = img.shape
    check = 0
    erosion_img = np.zeros((h_img, w_img), np.uint8)
    
    for i in range(h_img):
        for j in range(w_img):
            if img[i][j] == 255:
                flg = 1

                for y in range(h_se):
                    if flg == 0: 
                        break
                    for x in range(w_se):
                        if flg == 0: 
                            break
                        my_x = (j - w_se//2) + x
                        my_y = (i - h_se//2) + y

                        if my_y in range(h_img) and my_x in range(w_img) and img[my_y][my_x] != 255:
                            flg = 0
                if flg == 1:
                    erosion_img[i][j] = 255
    return erosion_img

erosion_pic = Erosion(img, SE)
cv2.imshow('pika_erosion_22', erosion_pic)
cv2.imwrite('output/pika_erosion_22.bmp', erosion_pic)
cv2.waitKey()


# In[7]:


name = 'input/pika.jpg'
# name = 'input/gun.bmp'
# name = 'input/palm.bmp'

SE = [6,6]
img = cv2.imread(name, 0)

def Dilation(img, SE):
    SE = np.ones((SE[0],SE[1]), np.uint8) * 255
    h_se, w_se = SE.shape
    h_img, w_img = img.shape
    check = 0
    dilation_img = np.zeros((h_img, w_img), np.uint8)
    
    for i in range(h_img):
        for j in range(w_img):
            if img[i][j] == 255:
                for y in range(h_se):
                    for x in range(w_se):
                        my_x = (j - w_se//2) + x
                        my_y = (i - h_se//2) + y

                        if my_y in range(h_img) and my_x in range(w_img):
                            dilation_img[my_y][my_x] = 255
    return dilation_img

dilation_pic = Dilation(img, SE)
cv2.imshow('pika_dilation_66', dilation_pic)
cv2.imwrite('output/pika_dilation_66.bmp', dilation_pic)
cv2.waitKey()


# In[12]:


# name = 'input/pika.jpg'
# name = 'input/gun.bmp'
# name = 'input/palm.bmp'

SE = [3,3]
img = cv2.imread(name, 0)

def Opening(img, SE):
    opening_img_1 = Erosion(img, SE)
    opening_img_2 = Dilation(opening_img_1, SE)
    return opening_img_2

opening_pic = Opening(img, SE)
cv2.imshow('palm_opening_33', opening_pic)
cv2.imwrite('output/palm_opening_33.bmp', opening_pic)
cv2.waitKey()


# In[16]:


# name = 'input/pika.jpg'
# name = 'input/gun.bmp'
name = 'input/palm.bmp'

SE = [3,3]
img = cv2.imread(name, 0)

def Closing(img, SE):
    closing_img_1 = Dilation(img, SE)
    closing_img_2 = Erosion(closing_img_1, SE)
    return closing_img_2

closing_pic = Closing(img, SE)
cv2.imshow('palm_closing_33', closing_pic)
cv2.imwrite('output/palm_closing_33.bmp', closing_pic)
cv2.waitKey()


# In[22]:


name = 'input/pika.jpg'
# name = 'input/gun.bmp'
# name = 'input/palm.bmp'

img = cv2.imread(name, 0)

def Boundary(img):
    boundary_img = Erosion(img, [3,3])
    b = img - boundary_img
    return b

img = Dilation(img, [6,6])
boundary_pic = Boundary(img)
cv2.imshow('updated_pika_boundary_33', boundary_pic)
cv2.imwrite('output/updated_pika_boundary_33.bmp', boundary_pic)
cv2.waitKey()


# In[ ]:




