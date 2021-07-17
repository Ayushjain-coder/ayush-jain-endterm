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

import cv2
from  PIL import Image, ImageOps

image1 = cv2.imread('img1.PNG') 
image2 = cv2.imread('img2.PNG')

drop_down = 'Addition' #@param["Addition", "Subtraction"]

def import_and_predict(image_data1, image_data2):
   
  if drop_down == "Addition":
    image_data = cv.add(image_data1,image_data2)

  if drop_down == "Subtraction":
    image_data = cv.subtract(image_data1,image_data2)  

  st.image(image_data, use_column_width=True)
  return 0
    
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
