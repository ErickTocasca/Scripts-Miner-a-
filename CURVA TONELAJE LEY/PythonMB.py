import matplotlib.pyplot as plt
from matplotlib.pylab import *
import numpy as np
import pandas as pd
datos = pd.read_csv('MBOK.csv', delimiter=';')

df=pd.DataFrame(datos)
print(df)

A=df.AU
T=df.TON
Ley=float(input('Ley de corte:'))

ip=[intervalo / 10 for intervalo in range(0,100,5)]
leyc=[]
tonelaje=[]
for i in range(len(ip)):
    ton=[]
    Aj=[]
    for j in range(len(A)):
        a=A[j]
        b=ip[i]
        if a>=b:
            ton.append(T[j])
            Aj.append(A[j])
            Ai=np.average(Aj,weights=ton)
            
            pass
    leyc.append(Ai)
    tonelaje.append(sum(ton))

fig2=plt.figure(facecolor='white')

plt.subplot(211,facecolor='lightyellow')
plt.suptitle('Curva Tonelaje - ley',color='blue')
ylabel('Tonelaje (TM)',color='blue',fontsize=8)
xlabel('ley de AU',color='red')
plt.plot(ip,tonelaje,label='Tonelaje (TM)')
plt.axvline(Ley,color='red',linestyle='dashed')
legend()
grid()

plt.subplot(212,facecolor='lightyellow')
plt.plot(ip,leyc,color='red',label='AU')
ylabel('Ley Media de AU',color='red',fontsize=8)
xlabel('ley de AU',color='red')
plt.axvline(Ley,color='red',linestyle='dashed')
legend()
grid()



            