from classes import *
from uteis import *

'''Lista de demandas máximas para os consumidores'''
demandaMaxima15min_1 = [
    12.4,13.4,16.1,12.9,11.9
]

demandaMaxima15min_2 = [
    10.1,12.9,13.8,14.2,16.3,14.3
]

demandaMaxima15min_3 = [
    17,15.1,16.7,18.3,17.3,16.1,17
]

'''Criação dos objetos'''
T1 = transformador(25,0.9,[1.8,40],demandaMaxima15min_1,2.4,V_secundario=0.24)
T2 = transformador(37.5,0.9,[1.9,45],demandaMaxima15min_2,2.4,V_secundario=0.24)
T3 = transformador(50,0.9,[2,50],demandaMaxima15min_3,2.4,V_secundario=0.24)


'''1) questão: '''
print('Demandas não diversificadas: ')
print(f'T1:   {T1.Dmax_não_div:.2f}')
print(f'T2:   {T2.Dmax_não_div:.2f}')
print(f'T3:   {T3.Dmax_não_div:.2f}')
print('')
print('Demandas diversificadas: ')
print(f'T1:   {T1.Dmax_diversificado:.2f}')
print(f'T2:   {T2.Dmax_diversificado:.2f}')
print(f'T3:   {T3.Dmax_diversificado:.2f}')

print('-'*30)
'''2) questão: '''
N1_N2 = alimentador([T1,T2,T3],2.4)
N2_N3 = alimentador([T2,T3],2.4)
N3_N4 = alimentador([T3],2.4)

print('Trecho N1 - N2')
print(f'Demanda não diversificada: {N1_N2.D_não_diversificada_max:.2f}')
print(f'Demanda diversificada: {(N1_N2.Dmax_diversificado):.2f}')
print('-'*30)

print('Trecho N2 - N3')

print(f'Demanda não diversificada: {N2_N3.D_não_diversificada_max:.2f}')
print(f'Demanda diversificada: {(N2_N3.Dmax_diversificado):.2f}')
print('-'*30)

print('Trecho N3 - N4')
print(f'Demanda não diversificada: {(N3_N4.D_não_diversificada_max):.2f}')
print(f'Demanda diversificada: {(N3_N4.Dmax_diversificado):.2f}')
print('-'*30)

# print(f'Fator de alocação {N1_N2.fator_alocação}')

print('-'*30)
'''3) questão: '''
'''--------------------------------------------------------------------------------------'''
linha_1 = N1_N2
linha_2 = N2_N3
linha_3 = N3_N4


linha_1.dadosLinha = complex(0.2841,0.5682)
linha_2.dadosLinha = complex(0.0284,0.0568)
linha_3.dadosLinha = complex(0.0426,0.8052)

'--------------------------Linha 1---------------------------------------------------------------'
linha_1.V_alimentador = complex(2.400,0)
linha_1.perdasLinha()
print(f'Tensão de saída: {abs(linha_1.V_saída):.2f}/__{angulo(linha_1.V_saída):.2f}')
print(f'Corrente na linha 1: {abs(linha_1.I_linha):.2f}/__{angulo(linha_1.I_linha):.2f}')
print(T1.tensão_secundário(linha_1.V_saída))
print('-'*30)
'--------------------------Linha 2---------------------------------------------------------------'
linha_2.V_alimentador = linha_1.V_saída/1000
linha_2.perdasLinha()
print(f'Tensão de saída: {abs(linha_2.V_saída):.2f}/__{angulo(linha_2.V_saída):.2f}')
print(f'Corrente na linha 2: {abs(linha_2.I_linha):.2f}/__{angulo(linha_2.I_linha):.2f}')
print('-'*30)
'--------------------------Linha 3---------------------------------------------------------------'
linha_3.V_alimentador = linha_2.V_saída/1000
linha_3.perdasLinha()
print(f'Tensão de saída: {abs(linha_3.V_saída):.2f}/__{angulo(linha_3.V_saída):.2f}')
print(f'Corrente na linha 3: {abs(linha_3.I_linha):.2f}/__{angulo(linha_3.I_linha):.2f}')
print('-'*30)
