import numpy as np
import pylab as pl
# Crea un vector (arreglo) con los valores del eje X
x = [1,2,3,4]
# Crea un vector (arreglo) con los valores en el eje Y para cada valor en el eje X
y = [7.25,8,9.2,5]
#Con esta isntruccion colocamos un titulo al eje Y de la grafica. 
pl.ylabel('Promedio por semestre')
pl.xlabel('semestre')
# Grafica el vector x contra el vector y
pl.axis ([0,5, 0,10])
pl.plot(x,y, 'r*')
#Guarda la grafica en el formato png
pl.savefig('temp2.png')
pl.show()
