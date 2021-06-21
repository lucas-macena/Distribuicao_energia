

class cliente:
    def __init__(self,demanda,s_instalada):
        self.Demanda = demanda
        self.S_instalada = float(s_instalada)

        self.Demanda_Máx = float(max(self.Demanda,key=float))

        soma_Demanda = 0

        for i in range(0,len(self.Demanda)):
            soma_Demanda += float(self.Demanda[i])


        self.Demanda_Méd = soma_Demanda/len(self.Demanda)

        self.F_demanda = self.Demanda_Máx/self.S_instalada

        try:
            self.F_carga = self.Demanda_Méd / self.Demanda_Máx
        except:
            self.F_carga = 0


clientes = list()
clientes.append("labels")

demanda_sistema = list()
demanda_sistema.append("labels")

Demanda_clientes = list()

def soma_sistema(demanda_intervalo):
    soma = 0

    for i in demanda_intervalo:
        soma+=float(i)

    demanda_sistema.append(soma)