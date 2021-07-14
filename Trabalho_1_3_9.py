import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

demanda = pd.read_csv('data.csv').T.to_numpy()

ramal1_consumidores = [55,56,57,58]
ramal2_consumidores = [54]
ramal3_consumidores = [47,48,49,50,51,52,53]
ramal4_consumidores = [13,21,33,35,36,37,44,46]
ramal5_consumidores = [2,3,4,7,8,11,12,16,17,18,22,27,30,45]
ramal6_consumidores = [5,10,28,31,41]
ramal7_consumidores = [6,9,14,15,19,20,23,24,25,26,29,32,34,38,39,40,42,43]

ramal_distribuicao = [54,55,56,57,58,47,48,49,50,51,52,53,13,21,33,35,36,37,44,
                      46,2,3,4,7,8,11,12,16,17,18,22,27,30,45,5,10,28,31,41,
                      6,9,14,15,19,20,23,24,25,26,29,32,34,38,39,40,42,43]

ramal1 = [demanda[i] for i in ramal1_consumidores]
ramal1 = sum(ramal1)
plt.plot(ramal1, color = 'red', label = 'Ramal 1')
plt.title('Curva de demanda diversificada - Ramal 1')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

ramal2 = demanda[54]
plt.plot(ramal2, color = 'red', label = 'Ramal 2')
plt.title('Curva de demanda diversificada - Ramal 2')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

ramal3 = [demanda[i] for i in ramal3_consumidores]
ramal3 = sum(ramal3)
plt.plot(ramal3, color = 'red', label = 'Ramal 1')
plt.title('Curva de demanda diversificada - Ramal 3')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

ramal4 = [demanda[i] for i in ramal4_consumidores]
ramal4 = sum(ramal4)
plt.plot(ramal4, color = 'red', label = 'Ramal 1')
plt.title('Curva de demanda diversificada - Ramal 4')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

ramal5 = [demanda[i] for i in ramal5_consumidores]
ramal5 = sum(ramal5)
plt.plot(ramal5, color = 'red', label = 'Ramal 1')
plt.title('Curva de demanda diversificada - Ramal 5')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

ramal6 = [demanda[i] for i in ramal6_consumidores]
ramal6 = sum(ramal6)
plt.plot(ramal1, color = 'red', label = 'Ramal 1')
plt.title('Curva de demanda diversificada - Ramal 6')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

ramal7 = [demanda[i] for i in ramal7_consumidores]
ramal7 = sum(ramal7)
plt.plot(ramal7, color = 'red', label = 'Ramal 1')
plt.title('Curva de demanda diversificada - Ramal 7')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

ramalD = [demanda[i] for i in ramal_distribuicao]
ramalD = sum(ramalD)
plt.plot(ramalD, color = 'red', label = 'Ramal D')
plt.title('Curva de demanda diversificada do sistema')
plt.xlabel('Horas')
plt.ylabel('Demanda [kW]')
plt.show()

curva_duracao = np.sort(ramalD)
curva_duracao = curva_duracao[::-1]
#plt.plot(curva_duracao, color = 'red', label = 'Ramal D')
#plt.title('Curva de demanda diversificada do sistema')
#plt.xlabel('Horas')
#plt.ylabel('Demanda [kW]')
#plt.show()
#y = curva_duracao
#x = np.arange(100)

#plt.hist(curva_duracao, bins = int(180/5), orientation = 'horizontal')

#print(curva_duracao)
