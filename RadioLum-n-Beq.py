import streamlit as st
import pandas as pd 
C_1 = 6.266e+18   # in CGS unit  
C_3 = 2.368e-03   # in CGS unit  
pi=3.14159 
#file upload and read

#  #####
def Beq(V,alpha,z,D_L,nuo, So_nuo,gamma_1, gamma_2):  
  Term_01 = (16*pi/V) 
  Term_02 = C_1**(1-alpha)/C_3  
  Term_03 = (4*pi*D_L**2)/(1-2*alpha)  
  Term_04 = (So_nuo*nuo**alpha)/((1+z)**(1-alpha))   

st.write("output") 
