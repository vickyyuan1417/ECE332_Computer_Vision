#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np
import collections
    
def TwoPass(name):
    img = cv2.imread(name, 0)
    # ensure binary
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    
    num_part = 0
    labeled_img = []
    h, w = img.shape
    labels = [[0 for i in range(w)] for j in range(h)]
    
    # A table for holding all pixel of img
    W_img = collections.defaultdict(int)

    # First pass
    for i in range(h):
        for j in range(w):
            if img[i][j] == 255:
                if (i-1) in range(h):
                    upper = labels[i-1][j]
                else:
                    upper = 0
                    
                if (j-1) in range(w):
                    left = labels[i][j-1]
                else:
                    left = 0
                # define all left and upper    
                    
                if upper == 0 and left == 0:
                    num_part += 1
                    labels[i][j] = num_part
                    
                elif left == 0 or upper == 0:
                    labels[i][j] = max(upper, left)
                    
                elif left == upper:
                    labels[i][j] = upper
                    
                else:
                    labels[i][j] = min(upper, left)
                    W_img[max(upper, left)] = max(W_img[max(upper, left)], labels[i][j])

    # Second pass
    def find_smallest_label(node):
        if node not in W_img:
            myset.add(node)
            return node
        else:
            return find_smallest_label(W_img[node])
    
    areas = collections.defaultdict(int)
    collected_pixel = collections.defaultdict(int)
        
    myset = set()

    for val in W_img:
        W_img[val] = find_smallest_label(W_img[val])
        


    dict = collections.defaultdict(int)
    
    for index, num in enumerate(myset):
        dict[num] = index + 1

    for i in range(h):
        for j in range(w):
            if img[i][j] == 255 and labels[i][j] in W_img:
                labels[i][j] = W_img[labels[i][j]]
                collected_pixel[labels[i][j]] += 1
            else:
                collected_pixel[labels[i][j]] += 1
                
    ###########################   
#     def filter():
        # this area can change to fitted one
        min_area = 2000
        for key in areas:
            if areas[key] < min_area:
                areas[key] = -1
            
    ############################
    labeled_img = img
    for i in range(h):
        for j in range(w):
#             filter()
            if labels[i][j]:
                if areas[labels[i][j]] == -1:
                    color = 0
                else:
                    color = 255/(len(myset)+1) * dict[labels[i][j]]
                labeled_img[i][j] = color
    ###########################
#     print(img)

#     label_hue = np.uint8(179 * img/np.max(img))
#     blank_ch = 255 * np.ones_like(label_hue)
#     labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

#     # cvt to BGR for display
#     labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

#     # set bg label to black
#     labeled_img[label_hue==0] = 0

    
    print('Nums:', len(myset))
#     cv2.imwrite('labeled.png', labeled_img)
    cv2.imshow('labeled.png', labeled_img)
    cv2.waitKey()


# In[ ]:


TwoPass("test.bmp")
# TwoPass("face.bmp")
# TwoPass("gun.bmp")
# TwoPass("face_old.bmp")


# In[ ]:




