from math import sqrt,pow

area_triangulo = 2 * 0.5 * 0.5 * 1.5
hipotenusa_triangulo = sqrt(pow(1.5,2) + pow(0.5,2))
area_retangulo = 2 * 0.5 * hipotenusa_triangulo

print(area_triangulo)
print(area_retangulo)

densidade_de_carga = 2.5 # MVA/milha²
fp = 0.9
V_nominal = 13.8 # kV

