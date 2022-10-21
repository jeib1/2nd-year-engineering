#Parte B
import numpy as np
import matplotlib.pyplot as plt

def ec1(x):
    return 1-x[0]-x[1]-k1*x[0]*(x[1]**2)  #Función que simula nuestra primera EDO; da/dt
def ec2(x):
    return k1*x[0]*(x[1])**(2)-k2*(x[1]**alpha)*(1-x[0]-x[1])  #Función que simula nuestra segunda EDO; dm/dt

def euler1(dt,x):
    return dt*ec1(x)  #Computa al aproximación de Euler para la primera EDO
def euler2(dt,x):
    return dt*ec2(x)  #Computa al aproximación de Euler para la segunda EDO

T=100  #El límite superior del intervalo (en millones de años)
h=0.1  #Se define delta t
N=int(T/h) #Se define la cantidad de elementos del arreglo

# Se crea un ''lienzo en blanco'' para empezar a trabajar las funciones con el Metodo Euler
# Se utiliza np.zeros, el cual nos crea un arreglo de N ceros
a_euler=np.zeros(N)
m_euler=np.zeros(N)

def me():  #Se define el Metodo de Euler como 'me' 
    for j in range(1,N):  #El 'for' itera nuestro metodo en el rango dado
        a_euler[j]=a_euler[j-1]+euler1(h,[a_euler[j-1],m_euler[j-1]])  #Se ocupa y[n]=y[n-1]+euler1[y[n-1]]
        m_euler[j]=m_euler[j-1]+euler2(h,[a_euler[j-1],m_euler[j-1]])  #Se ocupa y[n]=y[n-1]+euler2[y[n-1]]
  
#Se crea la figura
fig = plt.figure(figsize=(18,21))
fig.tight_layout()

# Se define un arreglo de tiempo con linspace
t=np.linspace(0,T,N)

#Se grafican los datos para cada caso de la tabla, con sus respectivas constantes

#Caso 1
#Se definen las constantes
k1=k2=10  
alpha=1

#Los valores iniciales
a_euler[0]=0.15
m_euler[0]=0.15

#Se pone a correr el metodo
me()

#Graficamos el plano de fases (a,m)
ax= plt.subplot(3,2,1)
ax.plot(a_euler, m_euler)

#Se crea el titulo, la leyenda y las etiquetas de los ejes
ax.set_title('Plano de fases para método de Euler (alpha = 1.0)',fontsize=15)
ax.set_xlabel('Masa de gas atómico (a)',fontsize=13)
ax.set_ylabel('Masa de gas molecular (m)',fontsize=13)

#Caso 2

#Se definen las constantes
k1=8
k2=15
alpha=1.2
'''Para este caso, se obtienen valores fuera de nuestro rango, es decir, nuestro metodo diverge, 
para solucionar esto, se disminuye el paso del tiempo de h=0.1 a h=0.01, de esta forma se logra
converger a los datos'''

#Nuevo delta t
h=0.01

#Nueva cantidad de elementos al variar 'h
N=int(T/h)

#Nuevo arreglo de tiempo para el nuevo 'h'
t1=np.linspace(0,T,N)

#Nuevo arreglo de N ceros
a_euler=np.zeros(N)
m_euler=np.zeros(N)

#Se definen las condiciones iniciales
a_euler[0]=0.4
m_euler[0]=0.3

#Arranca el metodo
me()

#Graficamos el plano de fases (a,m)
ax= plt.subplot(3,2,2)
ax.plot(a_euler, m_euler)

#Se crea el titulo, la leyenda y las etiquetas de los ejes
ax.set_title('Plano de fases para método de Euler (alpha = 1.2)',fontsize=15)
ax.set_xlabel('Masa de gas atómico (a)',fontsize=13)
ax.set_ylabel('Masa de gas molecular (m)',fontsize=13)

#Caso 3
'''Al variar los datos para el caso anterior, se volveran a definir con 'h'=0.1 para los siguientes casos'''

#Se definen las nuevas constantes (se mantiene k1y k2 del caso anterior)
alpha=1.5

#Volvemos a delta t=0.1 y sus respectivos arreglos
h=0.1
N=int(T/h)
a_euler=np.zeros(N)
m_euler=np.zeros(N)

#Valores iniciales
a_euler[0]=0.4
m_euler[0]=0.3

#Arreglo de tiempo con h=0.1
t=np.linspace(0,T,N)

#Arranca el metodo
me()

#Graficamos el plano de fases (a,m)
ax= plt.subplot(3,2,3)
ax.plot(a_euler, m_euler)


#Se crea el titulo, la leyenda y las etiquetas de los ejes
ax.set_title('Plano de fases para método de Euler (alpha = 1.5)',fontsize=15)
ax.set_xlabel('Masa de gas atómico (a)',fontsize=13)
ax.set_ylabel('Masa de gas molecular (m)',fontsize=13)

#Caso 4

#Nueva constante (solo varia alpha desde ahora)
alpha=1.9
me()

#Graficamos el plano de fases (a,m)
ax= plt.subplot(3,2,4)
ax.plot(a_euler, m_euler)


#Se crea el titulo, la leyenda y las etiquetas de los ejes
ax.set_title('Plano de fases para método de Euler (alpha = 1.9)',fontsize=15)
ax.set_xlabel('Masa de gas atómico (a)',fontsize=13)
ax.set_ylabel('Masa de gas molecular (m)',fontsize=13)

#Caso 5

#Nuevo alpha
alpha=2

#Arranca el metodo
me()

#Graficamos el plano de fases (a,m)
ax= plt.subplot(3,2,5)
ax.plot(a_euler, m_euler)


#Se crea el titulo, la leyenda y las etiquetas de los ejes
ax.set_title('Plano de fases para método de Euler (alpha = 2.0)',fontsize=15)
ax.set_xlabel('Masa de gas atómico (a)',fontsize=13)
ax.set_ylabel('Masa de gas molecular (m)',fontsize=13)

#Caso 6

#Nueva constante alpha
alpha=2.1

#Arrrancamos el metodo
me()

#Graficamos el plano de fases (a,m)
ax= plt.subplot(3,2,6)
ax.plot(a_euler, m_euler)

#Se crea el titulo, la leyenda y las etiquetas de los ejes
ax.set_title('Plano de fases para método de Euler (alpha = 2.1)',fontsize=15)
ax.set_xlabel('Masa de gas atómico (a)',fontsize=13)
ax.set_ylabel('Masa de gas molecular (m)',fontsize=13)