from math import sqrt,cos,sin,acos


K_drop = 0.00035291 #%/kVA.milha

n0_n1 = 1.5
n1_n2 = 0.75
n2_n3 = 0.5

S1 = 300
S2 = 750
S3 = 500

S_total = S1+S2+S3
V_nominal = 12.47*1000
I_T = S_total/V_nominal/sqrt(3)

dV_n3 = K_drop*100*(S3/1000)*0.5
print(dV_n3)