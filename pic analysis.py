import numpy as np
import cv2
from PIL import Image
from PIL.ImageDraw import ImageDraw

image = cv2.imread('Amoebe.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([22, 93, 0])
upper = np.array([45, 255, 255])
bw_image = cv2.inRange(image, lower, upper)

data = np.asarray(bw_image)
non_zero_indices = np.argwhere(data != 0)
Xc = non_zero_indices[:, 0].sum()
Yc = non_zero_indices[:, 1].sum()
Area = non_zero_indices.shape[0]

# Correction and calculation
Xc = Xc / Area + (1805 * 2346) / Area
Yc = Yc / Area + (2346 * 1098) / Area
print(Xc, Yc)

new = Image.open("Amoebe.jpg")
image_editable = ImageDraw(new)
image_editable.text((Xc - 254, Yc - 65), '''
                                          |
                                          |
                                          |
                                 ---------|---------
                                          |
                                          |
                                          |''', (255, 0, 0))
new.save("result.jpg")
