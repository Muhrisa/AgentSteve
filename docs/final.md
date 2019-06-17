---
layout:	default
title:	Final Report
---

## Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/k5p1342nWVI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Project Summary
ArchitectSteve is a tool that takes a photo of a building and constructs a 3D replica of it within the Minecraft environment. Our AI, Steve, processes the selected photo into an image matrix which is processed and then rendered into a 3D model approximating the structure. This subroutine is made possible using the external OpenCV shape detection resource from the pyimagesearch website. Using a filtering and processing pipeline in conjunction with the OpenCV library, we are able to extract an approximation of the buildings outline and thus subtract the background from the image through image segmentation and contouring.

After extracting the outline for the target building, we created an algorithm to extrapolate depth and convert the 2D image into a 3D structure. By exploiting assumptions of architectural geometry, we were able to use shape detection to create a layering of our 2D outline which results in a reasonable structure for the building being approximated.

ArchitectSteve processes the 2D image into a series of pixels (i.e., R{0-255} G{0-255} B{0-255}). These pixels are then translated into the Minecraft building block with the closest matching color. This process is aided by a dictionary of Minecraft blocks and associated colors (as seen and described from the website minecraft-ids.grahamedgecombe.com where the official names and coloring was taken from). After determining the approriate building block to use, ArichitectSteve displays the block at the appropriate coordinates in the Minecraft enviornment.

The result is a 3D appropriately colored block replica, in the Minecraft world environment, of the 2D building image that was “uploaded” to ArchitectSteve. Due to the height restriction of 256 blocks that exists in Minecraft, since the Minecraft world is made of 16x16x256 'chunks’, we resize the image so that the replicated structure would not be cutoff. The 2D building-view image also gets translated in order for the resulting replica to be perceived as having depth in Minecraft, thus having a 3D pop-up structure.

## Approaches
<img src="https://i.imgur.com/ffZ8HxM.png" width="500" height="300">
<img src="https://i.imgur.com/xsUe0pY.png" width="500" height="300">

We begin by selecting an image of a building using a quick Google Search. The GrabCut (Grab and Cut) algorithm, is an image segmentation method based on graph cuts, that uses OpenCV and Python in order to successfully automate a background removing subrouting for our images. 

Before we settled down on the GrabCut, we experimented with other ways of removing the background from an image, but these ways proved to only work proficiently a fraction of the time. The image segmentation works well for relatively simple images. We tried two relatively distinct GrabCut image segmentation approaches, but ultimately used approach #2.

__Approach #1:__

__1.__ apply a Gaussian Blur in order to reduce the noise in the original image, so that the noise in the edge detection is reduced

__2.__ run an edge detection subroutine, either a Sobel or Scharr gradient operators, on the image

__3.__ reduce the noise on the image by zeroing any value that is less than the mean of all the intensities that results from the edge detection algorithm

__4.__ run a contour detection subroutine over the edge detected image result and then smoothen the final contour

__Approach #2:__

__1.__ apply a Gaussian Blur in order to reduce the noise in the original image, so that the noise in the edge detection is reduced

__2.__ run an edge detection subroutine to find all the edges in the image using a pre-trained structured forest model for fast edge detection

__3.__ reduce the noise on the image by using median filters

__4.__ run a contour detection subroutine over the edge detected image result, finding the largest, most siginificant outer-most contour

__5.__ approximate contour to make a more accurate background and foreground differentiation 

In order to retrieve the RGB colors, we use the original image but first we flip the image. This is due to the fact that the objects were being built upside down in Minecraft whenever we passed the image in it's orginal upright orientation. Using this flipped image, we convert that image, using OpenCV, into a series of RGB values for each of the pixels in the image.

Using the shape detection, we then loaded the resultant image from the GrabCut algorithm, a binarized image, to analyze and identify the shapes via shape detection. We are using OpenCV’s shape contouring and detection functions. OpenCV recognizes shapes due to the difference in contrast, which is why we decided to use image processing and binarize the images so they have a white foreground against a black background.

We initially thought of breaking down the buildings into shapes and using OpenCV’s shape recognition, but we later realized that OpenCV can return the pixel coordinates for the perimeter of any polygon using the findContours function. We created a getArea() function using OpenCV’s pointPolygonTest() To test each pixel in the image and determine if those points are or are not within the shape. getArea() thus returns every coordinate where a block should be placed in the Minecraft world as a 2D object.

<img src="https://i.imgur.com/ttsqh9S.png" width="900" height="300">

To create a structure from our 2D matrix, we leveraged symmetry to create a layered depth effect. This algorithm is dependent on the accuracy of the outline we are able to extract which represents the shape of the building's facade. A total of n blocks are detected in the outline which form discrete vertical phases of the goal structure; each detected block will represent a unique depth layer. The center of the structure will contain all detected blocks and will represent the highest point of the building. This layer will be sandwiched between between a second layer which contains n-1 blocks because the topmost block is removed. This process continues as the layers cascade to the shortest layer, thus forming our 3D structure.


## Evaluation
__Qualitative Evaluation:__ ArchitectSteve does not attempt to produce an exact replica of the building captured in the original 2D image. We chose to render buildings in a Minecraft appropriate resolution rather than directly translating pixels to blocks. Additionally, we are not using external information about the specific building to transform it into a 3D structure. The only thing that ArchitectSteve knows is what the front view of the structures look like. Because of these factors, the AI's goal is to create a building structure inspired by the photo with a facade that is recognizable to the target photo.


<img src="https://i.imgur.com/M6RjrIh.png" width="500" height="300">


Our evaluation criteria is primarily focused on the qualitative factors, measured by the quality, size and appearance  of the building our algorithm created. To assess this part of the evaluation we perform a simple visual comparison between the 3D Minecraft colored block replica and the original 2D image. The dimension, depth, and color are three of the criteria we focused on, in order to create a much more realistic structure. As a result of the peer grading, we received positive feedback from other students solely on our accuracy of the building structure replication using only diamond blocks. 

<img src="blob:https://imgur.com/935ab019-9787-464e-85ae-a7703991b00c" width="1800" height="600">

The crux of the program is to develop an accuate outline on which the structure is to be based. We were able to evaluate the efficiency of the algorithm based on various image files generated thrughout the processing phase. The images above show an example of the outline as it is retrieved from the background removal pipeline. Because shadows, reflections, landscaping, etc. in the original photo can all significantly effect the resulting outline, additional processing is prefered to produce an outline which will more closely resemble a real building. We can observe these image files to determine whether the algorithm has produced a successful outline or not.

__Quantitative Evaluation:__ 
The evaluation criteria also includes a quantitative assessment that is focused on the extent of building images that it can successfully build replicas of. With the algorithm we have in place we are able to work with geometric structures that often resemble some kind of symmetry. We compare the results of asymmetrical building images and their replicas to symmetrical building images. The number of successful replicas is a lot higher for symmetrical structures.

<img src="https://i.imgur.com/V5onqdH.png" width="300" height="300">

## References
__Imutils:__ image processing functions such as translation, rotation, resizing, skeletonization, sorting contours and detecting edges with OpenCV and Python 3.

https://pypi.org/project/imutils/

__OpenCV Shape Detection:__ identify the contour or the outline of the shape using contour approximation in order to carry out shape detection. This approximation algorithm is commonly known as the Ramer-Douglas-Peucker algorithm. This essentially reduces the number of points on a curve or line to a simplified approximated version.

https://pypi.org/project/opencv-python/

https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/

__Minecraft Selfies:__ This resource is simlar to the Sketchy AI project that was created during the Spring of 2017 by Alex Chapp, Katherine Fitzpatrick, and Edwin Ho. The inspiration we drew from it, similar to the Sketchy AI, is the idea of rendering an image's colors in the form of pixels into Minecraft 3D structures. Reading through this resource we learned how to convert images into RGB values.

https://projects.raspberrypi.org/en/projects/minecraft-selfies/

__Resize Image:__ This was referenced when it came down to resizing the image due to the fact that Minecraft has a vertical limit, as explained above, therefore we had to resize or face an unexpected cutoff image as a result.

http://enthusiaststudent.blogspot.com/2015/01/horizontal-and-vertical-flip-using.html

__GrabCut:__ Background Removing algorithm.

https://en.wikipedia.org/wiki/GrabCut

https://www.codepasta.com/computer-vision/2016/11/06/background-segmentation-removal-with-opencv.html

https://www.codepasta.com/computer-vision/2019/04/26/background-segmentation-removal-with-opencv-take-2.html

__SketchyAI:__ Recreating images in Minecraft project created by Alex Chapp, Katherine Fitzpatrick, and Edwin Ho during the Spring of 2017.

https://alex561.github.io/Sketchy-AI/final.html

__Structured Forests:__ For the purpose of edge detection using machine learning from the OpenCV contribution below.
https://docs.opencv.org/3.1.0/d0/da5/tutorial_ximgproc_prediction.html
