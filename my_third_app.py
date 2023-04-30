import streamlit as st
import forallpeople as si
from app_module import calc_Comp
#si.environment("structural")


l_value = st.sidebar.number_input("Member length (mm)" , value=9690)
kex_value = st.sidebar.number_input("Effective length factor for Axial buckling" , value=0.7)
fy_value = st.sidebar.number_input("Steel yield strength (MPa)", value=230)
ag_value=st.sidebar.number_input("Gross area of the section (mm**2)", value=154355)
ah_value=st.sidebar.number_input("Area of the holes to be deducted (mm**2)", value=0)
r_value = st.sidebar.number_input("radius of Gyration (mm)", value=278.55)
Imin_value=st.sidebar.number_input("Minor MOI (mm**4)", value=11268.97E6)
Zemin_value=st.sidebar.number_input("Minor Secton modulus (mm**3)", value=32434E3)

phi = 0.9
l = l_value 
kex = kex_value
fy = fy_value
ag=ag_value
ah=ah_value 
r = r_value
Imin=Imin_value 
Zemin=Zemin_value 

mr_latex, mr_value = calc_Comp(ag, l, kex, ah, r, Imin, Zemin, phi, fy)

st.markdown("# Calculating the Axial compression capacity of a steel compact section as per AS 5100)")
st.latex(mr_latex)