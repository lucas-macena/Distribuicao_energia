import xlwt
import xlrd
import os
import csv

fatores_diversidade = [1.0, 1.0725423573110187, 1.1848670603372433, 1.2470395093660798, 1.2626534319167826, 1.227810064696714, 1.4757765425626987, 1.4757765425626987, 1.4901465177968767, 1.5990317735797046, 1.5228830519144663, 1.572651544647009, 1.694060736358098, 1.7454289906447376, 1.7451296173240705, 1.7123196103782907, 1.6912576217639281, 1.6912576217639281]

def DefinirDia(indice):
    x = indice - 11519

    codigoDia = int(x / 96)

    if codigoDia == 0:
        return "Domingo"

    if codigoDia == 1:
        return "Segunda"

    if codigoDia == 2:
        return "Terça"

    if codigoDia == 3:
        return "Quarta"

    if codigoDia == 4:
        return "Quinta"

    if codigoDia == 5:
        return "Sexta"

    if codigoDia == 6:
        return "Sábado"

def DefinirHora(indice):
    x = indice - 11519

    HoraMin = ((x/96)-int(x/96))*96*15

    Hora = int(HoraMin/60)
    Min = round(HoraMin % 60)

    return  str(Hora) + ':' + str(Min)

def DataHora(indice):

    return  str(DefinirDia(indice)) + ' ' + str(DefinirHora(indice))



def createWorkbook(name,dest):

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("Painel")
    dest = os.path.join(dest, f"{name}.xls")
    workbook.save(dest)
    print(f'\nArquivo Criado com sucesso.\nSalvo em {dest}\n')
    return [workbook,worksheet]

'''Classe de Objeto dos clientes'''
class cliente:

    def __init__(self,demanda,s_instalada):
        self.Demanda = demanda
        self.soma_Demanda = 0

        for i in demanda:
            self.soma_Demanda += float(i)

        self.Energia = self.soma_Demanda/4

        self.S_instalada = float(s_instalada)

        self.Demanda_Máx = float(max(self.Demanda,key=float))

        soma_Demanda = 0

        for i in range(0,len(self.Demanda)):
            soma_Demanda += float(self.Demanda[i])


        self.Demanda_Méd = soma_Demanda/len(self.Demanda)
        try:
            self.F_demanda = self.Demanda_Máx/self.S_instalada
        except:
            self.F_demanda = 0

        try:
            self.F_carga = self.Demanda_Méd / self.Demanda_Máx
        except:
            self.F_carga = 0

        self.encontrar_horario_demanda_máx()
        # self.hora_Demanda_Máx = self.Demanda.index(str(self.Demanda_Máx))



    def encontrar_horario_demanda_máx(self):
        n_leituras = len(self.Demanda)
        self.leitura_Demanda_Máx = 0
        if(self.Demanda_Máx == 0):
            self.leitura_Demanda_Máx = 11520

        else:
            for i in range(0,n_leituras):
                if self.Demanda_Máx == float(self.Demanda[i]):
                    self.leitura_Demanda_Máx = i + 11520

        self.hora_Demanda_Máx = DataHora(self.leitura_Demanda_Máx)


'''Criação da lista de clientes e ocupação da primeira posição para manter a numeração correta'''
clientes = list()
clientes.append("labels")

'''Criação da lista de demanda do sistema e ocupação da primeira posição para manter a numeração correta'''
demanda_sistema = list()
demanda_sistema.append("labels")

Demanda_clientes = list()

clientes_por_ramal=[list(),list(),list(),list(),list(),list(),list(),list()]

def soma_sistema(demanda_intervalo):
    '''
    Soma todas as demandas para aquele intervalo de tempo
    :param demanda_intervalo: lista de demandas dos 58 clientes para serem somadas
    :return: void
    '''
    soma = 0

    for i in demanda_intervalo:
        soma+=float(i)

    demanda_sistema.append(soma)

def escrever_dados_cliente(plan_resultados,posição,label,cliente):
    '''Escreve os resultados e dados do cliente na planilha de resultados'''
    plan_resultados.write(posição, 0, label)
    plan_resultados.write(posição, 1, cliente.S_instalada)
    plan_resultados.write(posição, 2, cliente.Demanda_Máx)
    plan_resultados.write(posição, 3, cliente.Demanda_Méd)
    plan_resultados.write(posição, 4, cliente.F_demanda)
    plan_resultados.write(posição, 5, cliente.F_carga)
    plan_resultados.write(posição, 6, cliente.leitura_Demanda_Máx)
    plan_resultados.write(posição, 7, cliente.hora_Demanda_Máx)
    plan_resultados.write(posição, 10, cliente.Energia)
    try:
        plan_resultados.write(posição, 8, cliente.Demanda_Máx_não_div)
        plan_resultados.write(posição, 9, cliente.F_diversidade)
        plan_resultados.write(posição, 12, cliente.DeMax_div_questao_8)
        return
    except:
        return