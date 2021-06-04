from diversity_factors import fatores_diversidade
from math import cos,sin,pi,atan,acos, atan2
from uteis import *

class transformador:
    def __init__(self,S_nominal=25,fator_potencia=0.9,impedancia=[0,0],demanda=[],V_nominal=13.8,V_primario=13.8,V_secundario=0.38):
        '''
        :param S_nominal: potencia nominal do trafo
        :param fator_potencia: fato de potencia do trafo
        :param impedancia: impedancia do trafo em pu
        :param demanda:
        :param V_nominal:
        '''
        self.Dmax=list()
        self.fator_potencia = fator_potencia #valor padrão
        self.S_nominal = S_nominal #25kVA padrão
        self.V_nominal = V_nominal
        self.V_secundario = V_secundario
        self.RT = self.V_nominal/self.V_secundario

        self.inserir_demanda_Max(demanda)
        self.fator_diversidade()
        self.calcularImpedancias(impedancia)
        self.calcularPotencias()

    def calcularPotencias(self):
        self.P_nominal = self.Dmax_diversificado
        self.Q_nominal = sin(acos(self.fator_potencia))*(self.P_nominal/self.fator_potencia)

    def calcularImpedancias(self,impedancia):
        '''
        calcula as impedancias do transformador associado
        :param impedancia: impedancia em forma de lista
        :return:
        '''
        self.Z_base = (self.V_nominal * self.V_nominal) * 1000 / self.S_nominal
        self.Z_pu = complex(impedancia[0]*cos(impedancia[1]*pi/180),impedancia[0]*sin(impedancia[1]*pi/180))
        self.Z_ohms = self.Z_base * self.Z_pu / 100

        self.R_ohms = self.Z_ohms.real
        self.X_ohms = self.Z_ohms.imag

    def inserir_demanda_Max(self,demanda):
        '''
        insere as demandas e atualiza a demanda máxima não diversificada
        :param demanda: lista com os valores de demanda a serem inseridos
        :return:
        '''
        for i in demanda:
            self.Dmax.append(i)
        self.Dmax_não_div = sum(self.Dmax)


    def fator_diversidade(self):
        '''
        busca na lista de fatores o correspondente ao numero de consumidores e calcula a demanda máxima diversificada com base neles
        :return: o fator utilizado para aquele transformador
        '''
        self.n_consumidores = len(self.Dmax)
        fator = fatores_diversidade[self.n_consumidores-1]
        self.Dmax_diversificado = self.Dmax_não_div/fator
        self.Smax_demanda_kVA = self.Dmax_diversificado/self.fator_potencia
        return fator

    def tensão_secundário(self,V_primário):
        self.V_primario = V_primário
        self.I_trafo = (complex(self.P_nominal,self.Q_nominal)/self.V_primario).conjugate()
        self.V_secundario = self.V_primario - self.I_trafo*self.RT*pow(self.Z_ohms,2)
        return self.V_secundario

class consumidor:
    consumo=0
    demanda=0

class alimentador:

    def __init__(self,trafos,V_nominal=13.8,fator_potencia=0.9,V_alimentador=[13800,0],dadosLinha=[0,0]):
        '''
        :param trafos:Inserir os transformadores na forma de lista
        :param V_nominal: tensão nominal do alimentador
        :param fator_potencia: fator de potencia do alimentador
        :param V_alimentador: tensões que entram no alimentador em forma de lista na forma POLAR
        :param dadosLinha: dados da linha de transmissão na forma de lista na forma POLAR em OHMS
        '''

        self.transformadores = trafos
        self.V_nominal = V_nominal
        self.fator_potencia = fator_potencia
        self.V_alimentador = polar2rect(V_alimentador[0],V_alimentador[1])
        self.dadosLinha = polar2rect(dadosLinha[0],dadosLinha[1])

        self.D_não_diversificada_max = 0
        self.n_clientes=0
        self.kVA_max = 0

        for i in trafos:
            self.D_não_diversificada_max += i.Dmax_não_div
            self.n_clientes += i.n_consumidores
            self.kVA_max += i.S_nominal

        self.calcularAlocação()
        self.calcularPotencias()
        self.perdasLinha()

    def calcularAlocação(self):
        '''
        Calcula a alocação utilizando os transformadores utilizados e a Demanda máxima diversificada encontrada
        :return:
        '''
        fator = buscar_Fator_Diversidade(self.n_clientes)
        self.Dmax_diversificado = self.D_não_diversificada_max/fator #tbm chamada de metered demand
        self.fator_alocação = self.Dmax_diversificado/self.kVA_max

        for T in range(0,len(self.transformadores)):
            self.transformadores[T].alocação = self.fator_alocação * self.transformadores[T].S_nominal


    def calcularPotencias(self):
        '''
        Calcula as potências do alimentador na forma complexa
        :return:
        '''
        self.P_nominal = self.Dmax_diversificado
        self.Q_nominal = (self.Dmax_diversificado/self.fator_potencia)*sin(acos(self.fator_potencia))
        self.S_nominal = complex(self.P_nominal,self.Q_nominal)

    def perdasLinha(self):
        '''
        Calcula as perdas na linha e a tensão na saída do alimentador
        :return:
        '''
        self.I_linha = (self.S_nominal / self.V_alimentador).conjugate()
        self.V_saída = self.V_alimentador*1000 - self.I_linha*self.dadosLinha


def buscar_Fator_Diversidade(n_consumidores):
    return fatores_diversidade[n_consumidores-1]

