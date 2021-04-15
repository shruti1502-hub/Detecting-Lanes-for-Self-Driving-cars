# Detecting-Lanes-for-Self-Driving-cars
This is a simple project for lane detection which is an important task for building models of self-driving cars. I have tried to detect lanes in images and videos using basics of Computer Vision and Hough Line Trandsforms.

# Concepts Used
1. Gray-Scaling: 
This is done to convert a 3-channel image to a single-channel image. Any image consists of three channels-RED,GREEN and BLUE. Processing an image with a single channel is easier as compared to a three-channel image; a grayscale image only consists of a single channel ranging from 0-255.

2. Gaussian Blur:
This is done to smoothen an image and remove the unecessary noise. 

3. Canny-Edge Detection:
This applies derivative-we use gradient in our image to measure sharp change in intensities in adjacent pixels in both x and y directions.

4. Hough-Line Transform:
The Hough transform is a feature extraction technique used in image analysis, computer vision, and digital image processing.The purpose of the technique is to find imperfect instances of objects within a certain class of shapes by a voting procedure. This voting procedure is carried out in a parameter space, from which object candidates are obtained as local maxima in a so-called accumulator space that is explicitly constructed by the algorithm for computing the Hough transform.

5. Final Processed Image:
![image](https://user-images.githubusercontent.com/67157901/114866761-98caeb00-9e11-11eb-9036-f5f934624e02.png)

