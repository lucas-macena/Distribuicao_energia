from math import log,pi,acos,sin,cos,sqrt


'''espaçamento dos condutores:'''
#em pés

D_ab=2.5
D_bc=4.5
D_ca=7.0

'''dados dos condutores'''

diametro=0.721 #inches
GMR=0.0244 #feets
resistividade=0.306 #ohm/mile
capacidade = 530

'''Determine a impedância de sequência positiva da linha em ohms/mile'''

D_eq = pow(D_ab*D_bc*D_ca,1/3)
z_positiva = complex(resistividade,0.12134*log(D_eq/GMR))

print(z_positiva)

'''------------------------------------------------------------'''
V_nominal = 12.47*1000
fp = 0.9
S = 1*1000*1000 #1MVA

I_3f = S/(V_nominal*sqrt(3))
I_3f = complex(I_3f*fp,I_3f*sin(-acos(fp)))

dV = (z_positiva*I_3f).real
V_fase = V_nominal/sqrt(3)
K_drop = 100*dV/V_fase
print(K_drop)

l=5 #milhas
S = 3 #3MVA
dV_percentual = K_drop*S*l
print(dV_percentual)