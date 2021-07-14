from math import log,pi,acos,sin,cos,sqrt


def polar2rect(Z,fi):
    return complex(Z*cos(fi*pi/180),Z*sin(fi*pi/180))

'''espaçamento dos condutores:'''
#em pés

D_ab=2.5
D_bc=4.5
D_ca=7.0

'''dados dos condutores'''

diametro=0.563 #inches
GMR=0.00814 #feets
resistividade=0.592 #ohm/mile
capacidade = 360

'''Determine a impedância de sequência positiva da linha em ohms/mile'''

D_eq = pow(D_ab*D_bc*D_ca,1/3)
z_positiva = complex(resistividade,0.12134*log(D_eq/GMR))


'''------------------------------------------------------------'''
'''Variáveis'''
V_nominal = 4160
fp = 0.9
S = 1*1000*1000 #1MVA

comprimentos = [0.15,0.175,0.2,0.125,0.225,0.125]
Potências = [200,150,100,300,425,500]

'''Corrente trifásica'''
I_3f = S/(V_nominal*sqrt(3))
I_3f = complex(I_3f*fp,I_3f*sin(-acos(fp)))

'''Queda de tensão por aproximação e K drop'''
dV = (z_positiva*I_3f).real
V_fase = V_nominal/sqrt(3)
K_drop = 100*dV/V_fase

'''K rise'''
I = polar2rect(abs(I_3f),90)
V_rise = abs((z_positiva*I/1000).real)
K_rise = (V_rise/(V_fase/1000))*100


'''Cálculo da queda de tensão no nó 6'''
soma_dV_percentual = 0
soma_Potencias = sum(Potências)/1000
for i in range(0,len(Potências)):
    soma_dV_percentual += K_drop * soma_Potencias * comprimentos[i]
    soma_Potencias -= Potências[i]/1000

'''Potência do capacitor'''
dV_desejada = 3 #%
dv_diferença = soma_dV_percentual-dV_desejada
soma_comprimentos = 0

for i in range(0,4):
    soma_comprimentos += comprimentos[i]
Q_cap = (dv_diferença/(K_rise*soma_comprimentos))*1000 #MVAr
# print(dv_diferença)

'''Exibir resultados'''
print(f'Impedância seq. pos.: {z_positiva:.2f}')
print(f'K drop: {K_drop:.2f}%')
print(f'K rise: {K_rise:.2f}%')
print(f'Queda de tensão percentual: {soma_dV_percentual:.2f}%')
print(f'Potência do banco de capacitores: {Q_cap:.2f} kVAr')
