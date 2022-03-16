import numpy as np
import cv2
from PIL import Image
from PIL.ImageDraw import ImageDraw

image = cv2.imread('Amoebe.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([22, 93, 0])
upper = np.array([45, 255, 255])
bw_image = cv2.inRange(image, lower, upper)

cv2.imwrite('bw picture.jpg', bw_image)
scan = Image.open("bw picture.jpg")

x = 0
Area = 0
Xc = 0
Yc = 0
while x < scan.width:
    y = 0
    while y < scan.height:
        pixel_value = scan.getpixel((x, y))
        if pixel_value == 255:
            Area += 1
            Xc += x
            Yc += y
        y += 1
    x += 1

Xc = Xc/Area+(1805*2346)/Area
Yc = Yc/Area+(2346*1098)/Area
print(Xc, Yc)

new = Image.open("Amoebe.jpg")
image_editable = ImageDraw(new)
image_editable.text((Xc - 254, Yc - 65),'''           
                                          |
                                          |
                                          | 
                                 ---------|---------
                                          |
                                          |
                                          |''', (255, 0, 0))
new.save("result.jpg")