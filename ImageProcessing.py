#!/usr/bin/env python
# coding: utf-8
# Author : Ahmad Rifki Fachrudin

# # <font color= "green">Python : Image Processing</font>

# ## <font Color = "red">Method 1</font>
# ## <font color = "blue">Using Pillow (PIL) Module</font>

# In[7]:


# importing PIL Module
from PIL import Image

# Read Image, which is in the same folder
img = Image.open('./burger.jpg')

# Display Image
img.show()


# ## <font Color = "red">Method 1.2</font>
# ## <font color = "blue">Using Pillow (PIL) with matplotlib Module</font>

# In[6]:


# importing PIL Module
from PIL import Image
# importing matplotlib Module
import matplotlib.pyplot as plt

# Read Image, which is in the same folder
img = Image.open('./burger.jpg')

# Using matplotlib module to display the image
plt.imshow(img)


# ## <font Color = "red">Method 2</font>
# ## <font color = "blue">Using matplotlib Module</font>

# In[5]:


# importing matplotlib Module
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read the image, whish is in the same folder
img = mpimg.imread('./burger.jpg')

# Display the image
plt.imshow(img)


# ## <font Color = "red">Method 3</font>
# ## <font color = "blue">Using imageio with matplotlib Module</font>

# In[4]:


# importing imageio Module
import imageio
# importing matplotlib Module
import matplotlib.pyplot as plt

# Read the image by imageio Module
img = imageio.imread('./burger.jpg')

#Display the image by using matplotlib
plt.imshow(img)


# ## <font Color = "red">Method 4</font>
# ## <font color = "blue">Using openCV Module</font>

# In[3]:


# importing opencv-python (cv2) Module
import cv2 as cv

#Read the image
img = cv.imread('./burger.jpg',1)
# NB: 1: cv.IMREAD_COLOR = to loads color image, transparency neglected
# 0: cv.IMREAD_GRAYSCALE = to loads image in grayscale mode
# -1: cv.IMREAD_UNCHANGED = to loads image including as such alpha channel

# Display image
cv.imshow('windowTitle', img)

# to display image until you press any key in keyboard
cv.waitKey(0)

# to destroy all windows
cv.destroyAllWindows()


# ## <font Color = "red">Method 5</font>
# ## <font color = "blue">Using openCV with matplotlib Module</font>

# In[2]:


# importing opencv-python (cv2) Module
import cv2 as cv
# importing matplotlib
import matplotlib.pyplot as plt

# Read the image in grayscale mode
img = cv.imread('./burger.jpg',0)
# convert from BGR color mode to RGB color mode
RGBimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Display image using matplotlib
plt.imshow(RGBimg)


# In[ ]:




