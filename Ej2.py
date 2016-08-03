
# coding: utf-8

# In[15]:

#Ejercicio Nina 3

#queremos abrir un archivo, y guardar la matriz de datos en otro archivo
#Abrimos el archivo donde estan los datos
entrada = open('nina3.data', 'r')
#Abrimos un archivo donde escribiremos lo que queremos extraer
salida = open('matriz.nina3','w')

#Palabra que queremos buscar para empezar a hacer el recorte
palabra1 = '1948'
#Palabra que queremos buscaqr para terminar de hacer el recorte
palabra2 = '2016'

#
while True:
    line=entrada.readline()
    if palabra1 in line:
        while True:
            line = entrada.readline()
            print(line)
            salida.write(line)
            if palabra2 in line:
                break
            if line == '':
                break
            
            #print(line)
            #salida.write(line)
    if line == '':
        break


# In[16]:

#Abrimos el nuevo archivo de texto
import numpy as np

datos = np.loadtxt('matriz.nina3') #abro los datos como matrix
print(datos)


# In[17]:

#Tenemos que reemplazar -99.99 por NaN
import pandas as pd
meses = ['ene','feb','mar','abr','mayo','jun','jul','ago','sep','oct','nov','dec']
datos1 = pd.DataFrame(datos[:,1:],index=datos[:,0],columns=meses)#con pandas permitimos que el array acepte otro tipo de dato
datos2 = datos1.replace('-99.99', np.nan) #reemplazo -99.99 por nan

print(datos2)


# In[18]:

#Calcular promedio 
#Por mes:
meanmes = np.nanmean(datos2,axis=0) #axis = 0  realiza el promedio por columna
meanmes


#por anio:
meananio = np.nanmean(datos2,axis=1) #axis = 1  realiza el promedio por fila
meananio





# In[19]:

#Calcular desvio standard
#Por mes:
stdmes = np.nanstd(datos2,axis=0) #axis = 0  realiza el promedio por columna
stdmes

#por anio:
stdanio = np.nanstd(datos2,axis=1) #axis = 1  realiza el promedio por fila
stdanio


# In[20]:

datitos = datos2.as_matrix()
#print(datitos)

dat = datitos[~np.isnan(datitos)]
print(dat)


# In[44]:

import matplotlib.pyplot as plt

plt.figure(figsize=(12,12),dpi=60)
plt.subplot(2,1,1)
plt.hist(dat,facecolor='r',alpha = 0.2)
plt.xlabel('TSM Ninio 3')
plt.ylabel('Frecuencia')
plt.title('Histograma de TSM')
#plt.show()

plt.subplot(2,1,2)
X = np.linspace(0,11,12,endpoint = True)
plt.plot(X,meanmes)
plt.xticks(X,meses)
plt.xlim([0,11])
plt.xlabel('meses')
plt.ylabel('TSM')
plt.title('Onda anual TSM')





# In[ ]:



