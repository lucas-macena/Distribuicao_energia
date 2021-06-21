from uteis import *
from Trabalho_uteis import *

path = os.path.abspath('')
path_clientes = os.path.join(path,'database','dados_clientes.xlsx')

"""Leitura do excel e criação de variáveis de controle"""
plan_clientes = xlrd.open_workbook(path_clientes)
sheet_S_instalada = plan_clientes.sheet_by_name('Carga instalada')
sheet_Demanda = plan_clientes.sheet_by_name('Demanda')

S_instalada = sheet_S_instalada.col_values(colx=0,start_rowx=0)


for i in range(1,sheet_Demanda.row_len(0)):
    Demanda_clientes.append(sheet_Demanda.col_values(colx=i,start_rowx=1))
    clientes.append(cliente(sheet_Demanda.col_values(colx=i,start_rowx=1),S_instalada[i]))

for i in range(1,len(sheet_Demanda.col_values(colx=1,start_rowx=1))):
    demanda_intervalo = sheet_Demanda.row_values(rowx=i,start_colx=1)
    soma_sistema(demanda_intervalo)


b = clientes[2].Demanda_Máx

print(b)
print(max(demanda_sistema[1:]))
