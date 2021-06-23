from uteis import *
from Trabalho_uteis import *

'''Definição dos diretórios de arquivos'''
path = os.path.abspath('')
path_clientes = os.path.join(path,'database','dados_clientes.xlsx')


"""Leitura do excel e criação de variáveis de controle"""
plan_clientes = xlrd.open_workbook(path_clientes)
sheet_S_instalada = plan_clientes.sheet_by_name('Carga instalada')
sheet_Demanda = plan_clientes.sheet_by_name('Demanda')

'''Offset na planilha para incluir posteriormente os resultados do sistema e dos ramais'''
offset = 8

"""Criação da planilha de resultados com os cabeçalhos, resultados é o excel e plan_resultados é a aba Painel criada"""
[resultados,plan_resultados] = createWorkbook('resultados',os.path.join(path,'database'))
plan_resultados.write(0, 0, "ID_cliente")
plan_resultados.write(0, 1, "S_instalada")
plan_resultados.write(0, 2, "Demanda_máx")
plan_resultados.write(0, 3, "Demanda_méd")
plan_resultados.write(0, 4, "F_demanda")
plan_resultados.write(0, 5, "F_carga")

'''Criação da lista de valores com a potência instalada'''
S_instalada = sheet_S_instalada.col_values(colx=1,start_rowx=0)
soma_S_instalada = 0

ramal_cliente = sheet_S_instalada.col_values(colx=2,start_rowx=0)

'''=============================================================================================================='''
'''=============================================================================================================='''
'''================================================CLIENTES======================================================'''
'''=============================================================================================================='''
'''=============================================================================================================='''

'''Criação dos objetos individuais para cada cliente com sua respectiva potencia instalada e curva de demanda'''
n_clientes = sheet_Demanda.row_len(0)
for i in range(1,n_clientes):

    '''Inclue na lista de Demandas dos clientes uma sublista com a Demanda do cliente i'''
    demanda_novo_cliente = sheet_Demanda.col_values(colx=i,start_rowx=1)
    Demanda_clientes.append(demanda_novo_cliente)

    """Cria o objeto cliente e atribui os valores de Demanda e a potencia instalada na lista de potencias instaladas"""
    novo_cliente = cliente(demanda_novo_cliente,S_instalada[i])

    '''Adiciona o novo cliente na lista de clientes'''
    clientes.append(novo_cliente)

    '''Escreve os resultados e dados do cliente na planilha de resultados'''
    plan_resultados.write(i+offset, 0, i)
    plan_resultados.write(i+offset, 1, novo_cliente.S_instalada)
    plan_resultados.write(i+offset, 2, novo_cliente.Demanda_Máx)
    plan_resultados.write(i+offset, 3, novo_cliente.Demanda_Méd)
    plan_resultados.write(i+offset, 4, novo_cliente.F_demanda)
    plan_resultados.write(i+offset, 5, novo_cliente.F_carga)

    '''Soma a potência do cliente à potencia total do sistema'''
    soma_S_instalada += float(S_instalada[i])

    '''Identifica o ramal do cliente e salva o objeto do cliente em uma lista com uma lista de clientes'''
    ramal = int(ramal_cliente[i])
    clientes_por_ramal[ramal].append(novo_cliente)


'''=============================================================================================================='''
'''=============================================================================================================='''
'''================================================SISTEMA======================================================='''
'''=============================================================================================================='''
'''=============================================================================================================='''

n_leituras = len(sheet_Demanda.col_values(colx=1,start_rowx=1))
for i in range(1,n_leituras):
    '''Soma da demanda do sistema completo percorrendo cada linha, ou seja, soma as 58 colunas e chama soma_sistema'''
    demanda_intervalo = sheet_Demanda.row_values(rowx=i,start_colx=1)
    soma_sistema(demanda_intervalo)


'''Criação do objeto cliente do Sistema completo'''
Sistema = cliente(demanda_sistema[1:],soma_S_instalada)

plan_resultados.write(1, 0, "Sistema")
plan_resultados.write(1, 1, Sistema.S_instalada)
plan_resultados.write(1, 2, Sistema.Demanda_Máx)
plan_resultados.write(1, 3, Sistema.Demanda_Méd)
plan_resultados.write(1, 4, Sistema.F_demanda)
plan_resultados.write(1, 5, Sistema.F_carga)

'''=============================================================================================================='''
'''=============================================================================================================='''
'''================================================RAMAIS========================================================'''
'''=============================================================================================================='''
'''=============================================================================================================='''


'''Criação dos ramais'''
Ramais = list()
Ramais.append('')


'''Percorre as listas de listas de ramais'''
for ramal in range(1,8):

    '''Criação da lista de demandas para o ramal da iteração'''
    demanda_ramal = list()
    demanda_ramal.append('')

    for intervalo in range(0,n_leituras):

        '''Criação das variáveis de soma associadas à potência instalada e a soma das demandas do ramal para o intervalo'''
        soma = 0
        soma_S_instalada = 0

        '''Número de clientes no ramal da iteração'''
        n_clientes_ramal = len(clientes_por_ramal[ramal])
        for id_cliente in range(0,n_clientes_ramal):

            '''Inclue o valor da demanda daquele cliente, para aquele intervalo no valor da demanda
               do ramal para aquele mesmo intervalo'''
            soma += float(clientes_por_ramal[ramal][id_cliente].Demanda[intervalo])

            '''Garante que a soma das potencias instaladas vai ocorrer apenas na última iteração,
               afim de garantir que não seja perdido processamento do computador à toa'''
            if intervalo == n_leituras-1:

                '''soma a potencia instalada do cliente ao valor total instalado no ramal'''
                soma_S_instalada += clientes_por_ramal[ramal][id_cliente].S_instalada

        '''Inclue o valor da soma daquele intervalo à lista de demanda para o ramal'''
        demanda_ramal.append(soma)

    '''Criação do objeto cliente do ramal com a lista de demandas e a soma de potência instalada'''
    novo_ramal = cliente(demanda_ramal[1:],soma_S_instalada)

    '''Adiciona o objeto de ramal à lista de objetos dos ramais'''
    Ramais.append(novo_ramal)

    '''Escreve os resultados daquele ramal na planilha de resultados'''
    plan_resultados.write(ramal+1, 0, "Ramal " + str(ramal))
    plan_resultados.write(ramal+1, 1, novo_ramal.S_instalada)
    plan_resultados.write(ramal+1, 2, novo_ramal.Demanda_Máx)
    plan_resultados.write(ramal+1, 3, novo_ramal.Demanda_Méd)
    plan_resultados.write(ramal+1, 4, novo_ramal.F_demanda)
    plan_resultados.write(ramal+1, 5, novo_ramal.F_carga)



"""Salva o arquivo do excel"""
path_to_save = os.path.join(path,'database','resultados.xls')
resultados.save(path_to_save)