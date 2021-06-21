import os
from datetime import datetime,timedelta
import clipboard
import xlwt
import xlrd
from math import cos,sin,pi,atan,acos, atan2

def mostrarLista(lista):
    for i in range(0,len(lista)):
        print(f'{lista[i]:.2f}')

def polar2rect(Z,fi):
    return complex(Z*cos(fi*pi/180),Z*sin(fi*pi/180))

def angulo(a,b=0):
    if type(a)==complex:
        arg = atan2(a.imag,a.real)*180/pi
    else:
        arg = atan2(b,a)*180/pi
    return arg

class P:
    def __init__(self,a,b):
        self.value = complex(a,b)
        self.polar=False
    def __call__(self, *args, **kwargs):
        if self.polar:
            print(self.value)



"""Cria uma saudação com base na hora informada"""
def saudacao():
    hora_atual = datetime.now().hour
    if hora_atual < 12:
        return 'Bom dia Lucas!'
    elif 12 <= hora_atual < 18:
        return 'Boa tarde Lucas!'
    else:
        return 'Boa noite Lucas!'

"""Cria um arquivo .txt ao se passar o nome"""
def createFile(nameFile):
    copiaNum = ''

    while True :
        try:
            file = open(nameFile +'.txt', 'x')
            file.close()
            nameFile = nameFile + '.txt'
            break
        except:
            copiaNum = 'b'
    print(f'Criado o arquivo: {nameFile}')
    return nameFile

"""Escreve e salva no arquivo .txt com base no caminho informado"""
def writeFile(nameFile,text):
    file = open(nameFile, 'w')
    file.write(text)
    file.close()

"""Lê e salva no arquivo .txt com base no caminho informado retornando a leitura em forma de array"""
def readFile(nameFile):
    file = open(nameFile,'r',encoding='utf8')
    text = file.readlines()
    file.close()
    for k in range(0,len(text)):
        text[k] = text[k].split("\n")[0]
    return text

"""Adiciona um texto à um arquivo preexistente"""
def appendFile(nameFile,text):
    file = open(nameFile, 'a')
    file.write(text)
    file.close()


def createWorkbook(name,dest):

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("Painel")
    dest = os.path.join(dest, f"{name}.xls")
    workbook.save(dest)
    print(f'\nArquivo Criado com sucesso.\nSalvo em {dest}\n')
    return [workbook,worksheet]



def showList(lista,totalFlag=0):
    for k in lista:
        print(k)
    print("")
    if totalFlag:
        print(f'Total: {len(lista)}')
        print("")
    print("-=" * 20)
    print("")
    return