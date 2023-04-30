from handcalcs.decorator import handcalc
from math import pi, sqrt
@handcalc()
def calc_Comp(ag: float, l: float, kex: float, ah: float, r: float, Imin: float, Zemin: float, phi: float, f_y: float):
    """
    Calculates Axial Capacity of a section as per AS 5100
    """
    L = l # Member Length
    K_axial = kex # Effective length factor
    L_E = L*K_axial # Effective length for axial buckling
    alpha_MX = 1 # Moment modification is considered as 1
    A_h = ah # Area of the holes being deducted
    R=r # radius of Gyration
    I_min=Imin # Minor axis Moment of Inertia
    Z_min=Zemin # Minor axis Section Modulus
    lambda_N = (L_E/R) * sqrt(f_y/250) # As per 10.3.3.(7)
    alpha_a = (2100*(lambda_N-13.5))/(lambda_N**2-15.3*lambda_N+2050) # As per 10.3.3.(8)
    lambda_m = lambda_N + 0 # As per 10.3.3.(5)
    neta = 0.00326*(lambda_m-13.5)
    if neta <= 0:
        neta = 0
    neta # As per 10.3.3.(6)
    Comp_m=((lambda_m/90)**2+1+neta)/(2*(lambda_m/90)**2) #Compression member factor as per 10.3.4(4)
    alpha_c=Comp_m*(1-sqrt(1-(90/(Comp_m*lambda_m))**2)) #Compression member slenderness reduction factor as per AS 10.3.3(3)
    N_s = (ag-ah)*f_y/1000 # Unfactored Axial capacity in kN
    N_cx=alpha_c*N_s # Unfactored Axial Compression capacity in kN
    Phi_N_cx=N_cx*phi
    return Phi_N_cx