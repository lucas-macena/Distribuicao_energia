
'''Classe de Objeto dos clientes'''
class cliente:
    def __init__(self,demanda,s_instalada):
        self.Demanda = demanda
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
