# Amoebe_RWTH_IAM
Hello!

The program creates a copy of the image named "result" with the center of mass marked with a red cross.
The coordinates are given in pixels and are (1598, 1339).

The Working Principle
It's as simple as it gets!
The program first checks the color of each pixel.
If the pixel is "yellowish" (i.e. the color value is in the range of typical values for the color "yellow"), the cv2.inRange() method sets its color to white, otherwise to black(bw picture.png).
This creates an image that is much easier to process (at least with the methods I've found).
The program then goes through the black and white image, checking for white pixels.
Then, using each white pixel as a mass 1 body, the program calculates the coordinates of the center of mass Xj = (Σmi*xij) / (Σmi). 
