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

R = st.slider('R', min_value=0, max_value=255, step=1)

import cv2
from  PIL import Image, ImageOps

image = np.ones((512,512,3), dtype = "uint8")*255

def import_and_predict(image_data): 
  image_data[:] = [R]
  st.image(image_data, use_column_width=True)
    
if st.button("Change Color"):
  result=import_and_predict(image)
  
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
