This assignment aims to histogram equalization of a gray image with more than 8 bits per pixel.
The provided image is called splash.png, which is a 10 bits gray image. As the image is stored in png format,
so the image is in mode 'I' when it is read into pillow Image object. 
for images other than those with 8 bit-depth, Image.histogram can not be used to get its histogram (one can verify this, by applying histogram() to the above image), in this case one can only rely on the histogram function provided by numpy.
After histogram is obtained for the image, histogram equalization mapping can then be calculated similar way as what is discussed in the class, except that we are now dealing with 10 bit-depth images.
Finally, histogram-equalized image can be obtained, the resulting image will be stored as he-splash.png.
So the assignment requires:
1. read in splash.png
2. collect its histogram
3. calculate histogram-equalization mapping
4. perform histogram equalization to the image
5. save the resulting image to he-splash.png
the prototype code is provided, and for turnning-in, implemented code, and the resulting image file should be submitted.
Some restrictions:
The histogram collected from the image is a strict image histogram.  
