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