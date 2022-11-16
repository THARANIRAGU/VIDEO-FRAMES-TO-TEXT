#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import logging
import os
import random
import string


# In[13]:


def length_of_video(video_path):
    "small helper function"
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


# In[14]:


length_of_video("C:/Users/Dell/Downloads/vkrp.mp4")


# In[15]:


save_path = "C:/Users/Dell/Desktop/output"
video_path = "C:/Users/Dell/Downloads/vkrp.mp4"


# In[16]:


def extracting_frame(video_path,save_path,
                    skip_frames = 100):
    cap = cv2.VideoCapture(video_path)
    count = 0
    
    ret,frame = cap.read()
    test_file_path = os.path.join(save_path,"vkrp"+'{}_{}'+str(count)+'.jpg')
    
    cv2.imwrite(test_file_path, frame)
    
    if os.path.isfile(test_file_path):
        count = 1
        while ret:
            ret,frame = cap.read()
            if ret and count % skip_frames == 0:
                cv2.imwrite(os.path.join(
                    save_path,"vkrp"+'{}_{}'+str(count)+'.jpg'),frame)
                count += 1
                print(count)
            else:
                count += 1
        else:
            if count > 1:
                print("saving completed")
            else:
                print('problem with saving')
            return 0
        cap.release()


# In[6]:


extracting_frame(video_path,save_path)


# In[17]:


# import the following libraries
# will convert the image to text string
import pytesseract	

# adds image processing capabilities
from PIL import Image	

# converts the text to speech
import pyttsx3		

#translates into the mentioned language
from googletrans import Translator	

# opening an image from the source path
img = Image.open("C:/Users/Dell/Desktop/output/vkrp{}_{}1500.jpg")	

# describes image format in the output
print(img)						
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('C:/Users/Dell/abc.txt',mode ='w') as file:	
	
				file.write(result)
				print(result)
				


# In[18]:


pip install deep_translator


# In[19]:


from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='english', target='tamil').translate_file('C:/Users/Dell/abc.txt')


# In[20]:


print(translated)


# In[ ]:




