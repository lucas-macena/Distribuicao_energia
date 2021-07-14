import pandas as pd
import numpy as np
import csv

'''Definição dos diretórios'''
import os
path = os.path.abspath('')
path_data = os.path.join(path,'database','data.csv')
path_Demanda_ramais = os.path.join(path,'database','DmaxNDivRamais.csv')
path_to_save_Q7 = os.path.join(path,'database','resultadoQuestao7.csv')

# PARA A DETERMNAÇÃO DA TABELA DE FD:

listaConsumidoresRamal = []
listaConsumidoresRamal = ["6", "9", "14", "15", "19", "20", "23", "24",
                          "25", "26", "29", "32", "34", "38", "39", "40", "42", "43"] #iniciar zerada na hora de rodar
#quantidadeConsRamal = int(input('Digite a quantidade de consumidores do maior ramal: '))
quantidadeConsRamal = len(listaConsumidoresRamal)

#for contador in  range(0,quantidadeConsRamal):
    #listaConsumidoresRamal.append(str(input(f'Digite o numero do consumidor {contador+1}: ')))

arquivo = pd.read_csv(path_data, sep = ',')
#print(arquivo.head())

consumidoresRamal = arquivo[listaConsumidoresRamal]
#print(consumidoresRamal.head())


listaDemaxConsumidor = []

for i in listaConsumidoresRamal:
    #print(consumidoresRamal[i].max())
    listaDemaxConsumidor.append(consumidoresRamal[i].max())

print('='*40)
print('Lista de Demanda Máxima de cada consumidor do maior ramal:\n {}' .format(listaDemaxConsumidor))
print('='*40)


listaDemaxDiversificada = []

#column_names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17", "18"]
#sum_column = pd.DataFrame(columns=column_names)
sum_column = pd.DataFrame()
for i in listaConsumidoresRamal:
    if sum_column.empty:
        sum_column = consumidoresRamal[i]
    else:
        sum_column += consumidoresRamal[i]
    #print(sum_column)
    listaDemaxDiversificada.append(sum_column.max())

print('Lista de Demanda Máxima Diversificada (considerando aumento'
      ' de um em um dos consumidores do maior ramal):\n {}' .format(listaDemaxDiversificada))
print('='*40)

somaDemaxNCoinc = 0
listasomaDemaxNCoinc = []

for i in range(0, quantidadeConsRamal):
    if somaDemaxNCoinc == 0:
        somaDemaxNCoinc = listaDemaxConsumidor[i]
    else:
        somaDemaxNCoinc += listaDemaxConsumidor[i]
    listasomaDemaxNCoinc.append(somaDemaxNCoinc)

print('Lista de Demanda Máxima Não Coincidente (considerando aumento'
      ' de um em um dos consumidores do maior ramal):\n {}' .format(listasomaDemaxNCoinc))
print('='*40)

calculoFD = 0
listaFD = []
for i in range(0, quantidadeConsRamal):
    calculoFD = (listasomaDemaxNCoinc[i])/(listaDemaxDiversificada[i])
    listaFD.append(calculoFD)

print('Lista de FD (fator de diversidade):\n {}' .format(listaFD))
print('='*40)


# PARA COMPARAR A DMÁX-DIV PELO MÉTODO COM A DMÁX-DIV REAL ENCONTRADA ANTERIORMENTE NA QUESTÃO 4:

arquivoQuestao4 = pd.read_csv(path_Demanda_ramais, sep = ',')
#print(arquivoQuestao4.head())
#quantidadeRamais = int(input('Digite a quantidade total de ramais: '))
#listaquantidadeCons = []
listaquantidadeCons = [4, 1, 7, 8, 14, 5, 18]
#for i in range(0, quantidadeRamais):
    #numeroCons = int(input(f'Digite a quantidade de consumidores do ramal {i+1}: '))
    #listaquantidadeCons.append(numeroCons)
print('Total de consumidores de cada ramal:{}'.format(listaquantidadeCons))

listaFDCons =[]
for i in range(0, len(listaquantidadeCons)):
    listaFDCons.append(listaFD[listaquantidadeCons[i]-1])
print(f'FD para cada ramal: {listaFDCons}')

listaDemaxDivCadaRamal = []
for  i in range(0,len(listaFDCons)):
    listaDemaxDivCadaRamal.append((arquivoQuestao4[str(i+1)].values[0])/listaFDCons[i])

print('='*40)
print('Demanda máxima diversificada (pelo método da questão 7): \n{}'.format(listaDemaxDivCadaRamal))

resultado = open(path_to_save_Q7, 'w', newline = '', encoding = 'utf-8')
write = csv.writer(resultado, delimiter = ',')

write.writerow(listaDemaxDivCadaRamal)













