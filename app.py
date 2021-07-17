import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)

html_temp = """
   <div class="" style="background-color:green;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing II - Midterm Examination</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)

st.title("""
        Arithmetic Operations
         """
         )

file1 = st.file_uploader("Please upload first image", type=("jpg", "png"))

file2 = st.file_uploader("Please upload second image", type=("jpg", "png"))

drop_down = 'Addition' #@param["Addition", "Subtraction"]

import cv2
from  PIL import Image, ImageOps

def import_and_predict(image_data1, image_data2):
   
  if drop_down == "Addition":
    image_data = cv.add(image_data1,image_data2)

  if drop_down == "Subtraction":
    image_data = cv.subtract(image_data1,image_data2)  

  st.image(image_data, use_column_width=True)
  return 0

if file1 is None or file2 is None:
  st.text("Please upload an Image file")
else:
  file_bytes1 = np.asarray(bytearray(file.read()), dtype=np.uint8)
  image1 = cv2.imdecode(file_bytes1, 1)

  file_bytes2 = np.asarray(bytearray(file.read()), dtype=np.uint8)
  image2 = cv2.imdecode(file_bytes2, 1)

  st.image(file,caption='Uploaded Image.', use_column_width=True)
    
if st.button("Change Image"):
  result=import_and_predict(image1,image2)
  
if st.button("About"):
  st.header(" Ayush Jain")
  st.subheader("Student")
html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image processing Mid Term Experiment</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
