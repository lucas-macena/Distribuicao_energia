from Trabalho_1_7 import *
from Trabalho_1_1 import *

plan_resultados.write(0, 11, "DeMáx_div_questão_7")
for i in range(0,len(listaDemaxDivCadaRamal)):
    plan_resultados.write(i + 2, 11, listaDemaxDivCadaRamal[i])

resultados.save(path_to_save)
