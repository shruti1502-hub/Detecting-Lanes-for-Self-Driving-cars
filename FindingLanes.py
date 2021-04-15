#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# # Edge Detection
# To identify the boundaries in images-identifying sharp changes in intensity in adjacemt pixels or sharp changes in pixels
# 
# At Edge- there is a rapid change in brightness

# # Gradient
# Measure in change in brightness in adjacent pixels
# 
# Strong Gradient- shows sharp change in brightness like from 0-255
# 
# Small Gradient- Shows small change in brigthness like from 0-15

# In[2]:


#First we need to convert our image to grayscale
#This is necessary because a normal image consists of three channels-Red,Green,Blue
#Each Pixel is a combination of three intensities

#Wheras in grayscale image- only has 1 channel;each pixel has only one intensity ranging from 0-255
#processing a single chnnel image is simpler than processsing a three-channl image


# In[3]:


#Apply Gaussian Blur:
#Reduce Noise

#to smoothen a image, we take average of all pixels around a image which is done by kernel



# In[4]:


#Applying Canny method
#applies derivative-we our applying gradient in our image to measure sharp cha ge in intesnities in adjacent pixels in both x and y directions

def make_coordinates(image, line_parameters):
    slope,intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-intercept)/slope)
    x2 = int((y2-intercept)/slope)
    return np.array([x1, y1, x2, y2])
    





def average_slope_intercept(image,lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters = np.polyfit((x1,x2), (y1,y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average = np.average(left_fit, axis = 0)
    right_fit_average = np.average(right_fit,axis= 0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line, right_line])
    
    
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur= cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny

def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2=line.reshape(4)
            cv2.line(line_image, (x1,y1), (x2,y2), (255, 0 ,0), 10)
            
    return line_image
    
    
    
    

def region_of_interest(image):
    height= image.shape[0]
    polygons = np.array([
        [(200,height), (1100,height), (550,250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image

image=cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny_image= canny(lane_image)
cropped_image = region_of_interest(canny_image)
lines=cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
averaged_lines = average_slope_intercept(lane_image, lines)
line_image = display_lines(lane_image,averaged_lines)
combo_image= cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

cv2.imshow("result",combo_image) #computing the bitwise and of both images takes the bitwise and of each pixel in both arrays,ultimateky masking the canny image to only show the region of interest
cv2.waitKey(0)


    
    
    


    
 #parameters are low an high threshold--low threshold images are ignored and high threshold are accepted in a certain conditions
#image lying brtween low and high threshold is accepted



#The output image traces and outline of edges that shows sharp changes in intensities
#gradients that exceed the threshold are traceed as high pixels
#small change in intesities lying below threshold are not traced at all and are left as black


# #
# we need to trace our region of interest.
# This is done by making a triangle-traced as foloows
# 1) 200 pixels along the x-axis, 700 pixels down the y-axis--reaching at a bottom point
# 
# 2) 1100 pixels along x-axis, 700 pixels down y-axis--reaching at a point on the x-axis
# 
# 3) 500 pixels along x-axis and 200 pixels down y-axis, completing the triangle.

# In[5]:


#Video
cap = cv2.VideoCapture(r'test2.mp4')

while(cap.isOpened()):
    
    _ , frame = cap.read()
    
    canny_image = canny(frame)
    
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image , 2 , np.pi/180 , 100 , np.array([]), minLineLength = 40 , maxLineGap = 5)
    
    averaged_lines = average_slope_intercept(frame , lines)
    line_image = display_lines(frame , averaged_lines)
    
    combo_image = cv2.addWeighted(frame , 0.8, line_image , 1, 1)
    
    cv2.imshow('result', combo_image)
    
    if cv2.waitKey(10) & 0xFF== ord('q'):
        
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




