#Lines 3-18 import the necessary libraries.

import json
import math
import requests
import numpy as np
import array as arr
import pandas as pd
from PIL import Image
#import seaborn as sns
import streamlit as st
#from st_aggrid import AgGrid          #Library used for creating interactive tables.
#import streamlit_modal as modal
import matplotlib.pyplot as plt
#from streamlit_lottie import st_lottie
#from annotated_text import annotated_text
#from streamlit_option_menu import option_menu
import base64
#The base64 libarary helps with the data download for the csv file because it is going to encode the ASCII to byte conversion.


#Function for LOTTIE GIF's to be used in the web application. Lines 23-28.
@st.cache(allow_output_mutation=True)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()


#Page configuration settings. Lines 32-35.
st.set_page_config(
    page_title = 'Traffic Flows Model',
    page_icon = '🏍'
)



#SIDEBAR initial information Lines 34-46.
with st.sidebar:
    url1 = "https://assets4.lottiefiles.com/packages/lf20_3e0g4gjg.json"
    res1_json = load_lottieurl(url1)
    st_lottie(res1_json)
    options = option_menu(
        menu_title = "Navigation",
        options = ["Introduction", "Assumptions", "Model Formulation", "References"],
        icons = ["info-circle-fill", "dice-6-fill", "building", "link-45deg"],
        menu_icon = "cast",
        default_index = 0)
        #orientation = "horizontal")                                      #Bootstrap icons used for navigation bar.                 
st.sidebar.write("***")
st.write("***")



#INTRODUCTION PAGE code. Lines 51-56 as of now.
if (options == 'Introduction'):
  st.title("MODELLING AND ANALYSIS OF TRAFFIC FLOWS")
  
  url2 = "https://assets9.lottiefiles.com/packages/lf20_useqtj8t.json"
  res2_json = load_lottieurl(url2)
  st_lottie(res2_json)
 
  st.write("Imagine you are in a plane and you look down below just before landing. The traffic looks almost similar to a stream of fluid. Quite a pleasant sight for the eyes if you ask me! But imagine, now you are in that same traffic, stuck for the past few hours. Not so pleasant is it?")

  url3 = "https://assets3.lottiefiles.com/packages/lf20_KuzQYT.json"
  res3_json = load_lottieurl(url3)
  st_lottie(res3_json)
    
  st.write("The above two POVs are quite similar to the models being developed by researchers since the beginning of the twentieth century to predict and understand traffic flows.") 



if (options == 'Assumptions'):
    st.title("ASSUMPTIONS")
    st.write("The system of equations was formulated while keeping in mind a set of assumptions. I will walk you through each one of them and by the end of this section, you will be looking at the **BLOCK DIAGRAM** of the **FBDF** model.")
    
    col1, col2 = st.columns(2)
    with col1:
         with st.expander("ASSUMPTION 1"): 
              st.write("***")  
              st.write("At any time, the vehicle population is **homogenously mixed**, that is, the blocked vehicles and free vehicles are always **randomly distributed** over the single road under consideration. Thus, every free vehicle is equally likely to get blocked, every blocked vehicle is equally likely to get discharged and every discharged vehicle is equally likely to get free. This assumption is necessary because otherwise one has to use a network-based approach which will explicitly model the heterogeneity of the free-blocked vehicles contact pattern.")
              st.write("***") 
         with st.expander("ASSUMPTION 3"):   
              st.write("***")
              st.write("Vehicle population is large enough to ignore **random fluctuations** between individual vehicles. This takes care of the fact that we do not end up with a stochastic model. Here I would like to point out that the FBDF model is **deterministic**.")
              st.write("***")
         with st.expander("ASSUMPTION 5"):
              st.write("***") 
              st.write("There are three compartments:")       
              st.latex("F(t), B(t), D(t)")
              st.write("***") 
         with st.expander("ASSUMPTION 7"):
              st.write("***")
              st.write("Vehicles may leave the present road to follow another route. The reasons could involve cutting down on time, etc. The following parameter takes this possibility into account:")
              st.latex("μ_{d}") 
              st.write("This is the rate at which vehicles go off the road. It is assumed that this parameter remains the same for all the three compartments. Or in other words we assumed that the rate at which free/blocked/discharged vehicles may leave the road is proportional to the number of free/blocked/discharged vehicles respectively ")  
              st.write("Thus, we can write,")
              st.write("1. The rate of free vehicles leaving the road = ")
              st.latex("-μ_{d}*F")
              st.write("2. The rate of blocked vehicles leaving the road = ")
              st.latex("-μ_{d}*B")
              st.write("3. The rate of discharged vehicles leaving the road = ")
              st.latex("-μ_{d}*D")
              st.write("***")  
    
    
    with col2:
         with st.expander("ASSUMPTION 2"):
              st.write("***")   
              st.write("2. **Rate of blocking is proportional to B** i.e.: the number of blocked vehicles. This assumption is the reason why the **non-linearity** comes into picture. More on this in assumption number 8.")
              st.write("***")  
         with st.expander("ASSUMPTION 4"):
              st.write("***")
              st.write("4. The blocking is propagated only by other blocked vehicles. We are not considering blockage due to other reasons say, a tree is obstructing the road or some construction work is going on. This means that in the initial conditions, B(0) has to be at least one for the **blocking steady state** to exist. This initial source of blocking could be something like, say a flat tire. But the rest of the vehicles will be blocked due to the other blocked vehicles **only**.")
              st.write("***")  
         with st.expander("ASSUMPTION 6"):
              st.write("***")
              st.write("The new vehicles will be joining the road at a constant rate 𝜏. This is essentially the growth rate of the free vehicles on the road. Also, it is assumed that the new vehicles joining the road will be free. They will not get blocked immediately. So, we are only considering the growth rate of free vehicles and not the growth rate of blocked vehicles")
              st.write("***")  
         with st.expander("ASSUMPTION 8"):
              st.write("***")
              st.write("To model the total rate of free vehicles getting blocked, we will consider the free vehicles blocked by a single blocked vehicle. It is evident that the greater number of free vehicles, the greater the increase in the number of blocked vehicles. Thus, the rate of free vehicles blocked by a single blocked vehicle will be an increasing function of the number of free vehicles. For simplicity, we assumed that this rate is directly proportional to the number of free vehicles. The number of free vehicles at time t is denoted by:")
              st.latex("F(t)")
              st.write("Then the rate of free vehicles getting blocked is:") 
              st.latex("λ(t)*F(t)")
              st.write("However, it is not reasonable to assume that 𝜆 is a constant, since the more blocked vehicles there are, the higher the possibility that a single free vehicle will get blocked. Thus, we can write, the rate of free vehicles getting blocked = ")
              st.latex("λ(t)*F(t)")
              st.write("λ is the per-capita rate at which free vehicles become newly blocked, and thus, for very small-time intervals,")  
              st.write("***")
    
    
if (options == 'References'):
  st.title("REFERENCES")


#https://medium.com/analytics-vidhya/solving-a-system-of-two-differential-equations-numerically-in-python-d31844d4ea28
#Learn Mayavi. What are VTK's? Blahahah
#https://www.sciencedirect.com/science/article/pii/S0191261521002101
#https://plotly.com/python/sliders/   Interactive plots.
