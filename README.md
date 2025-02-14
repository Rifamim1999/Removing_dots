
# Creation of a Focused Dataset

In this process, we process the images of the dataset. In Arabic letters, there are lot of dots both above and below the letters. So, the goal is to detect those dots and isolate them. This is done by using Morphological operations. 


## Morphological Operations

Morphological operations are techniques used in image processing that focus on the structure and form of objects within an image. It relies on two key elements:

•	**The input image:** The input image is a binary image. The objects of interest are represented by foreground pixels (white) and the background by black.

•	**The structuring element:** A small matrix or kernel that defines the neighborhood of pixels over which the operation is performed.

The key morphological operations are:

•	**Erosion:** It is the set of all points in the image where the structuring element “fits into”. It shrinks the foreground and enlarges the background.

•	**Dilation:** It is the set of all points in the image where the structuring element “touches or hits”. It enlarges the foreground and shrinks the background. 

•	**Opening:** It is known as compound operation. It operates by performing erosion and then dilation operations.

•	**Closing:** It is also a compound operation. It operates by performing dilation and then erosion.

**Algorithm: **

•	Converted the input image into the grey-scaled image.

•	Applied Gaussian Blur to reduce noise and smooth the image.

•	Then applied a binary threshold to create a binary image to make the background black and the foreground white

•	Performed Morphological opening operation to remove small noise and separate dots from the text.

•	Performed Morphological closing operation to merge fragmented regions of dots.

•	Found contours in the processed binary image to identify candidate regions (dots).

•	Applied area and aspect ratio filtering:

    o	Area filtering to keep only contours with the area below a threshold.
    o	Aspect ratio filtering to discard non-circular shapes by restricting the width-to-height ratio of bounding boxes.
•	Generated a binary mask where detected dots are marked.

•	Used Inpainting to fill the regions of the mask in the original image, blending the removed dots with surrounding pixels.


