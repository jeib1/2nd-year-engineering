#Parte C
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1-x[0]-x[1]-k1*x[0]*(x[1]**2) #Función que simula nuestra primera EDO; da/dt
def g(x):
    return k1*x[0]*(x[1])**(2)-k2*(x[1]**alpha)*(1-x[0]-x[1])  #Función que simula nuestra segunda EDO; dm/dt

def euler1(dt,x):
    return dt*f(x)  #Computa al aproximación de Euler para la primera EDO
def euler2(dt,x):
    return dt*g(x) #Computa al aproximación de Euler para la segunda EDO

T=150  #El límite superior del intervalo para el periodo limte (en millones de años)
h=0.1 #Se define delta t
N=int(T/h) #Se define la cantidad de elementos del arreglo
k1=8 #Se define k1
k2=15 #Se define k2

# Se crea un ''lienzo en blanco'' para empezar a trabajar las funciones con el Metodo Euler
# Se utiliza np.zeros, el cual nos crea un arreglo de N ceros
a_euler=np.zeros(N)
m_euler=np.zeros(N)

def me():  #Se define el Metodo de Euler como 'me' 
    for j in range(1,N):
        a_euler[j]=a_euler[j-1]+euler1(h,[a_euler[j-1],m_euler[j-1]])
        m_euler[j]=m_euler[j-1]+euler2(h,[a_euler[j-1],m_euler[j-1]])    
        
#Se busca el PERIODO LIMITE c/r a alpha 

#Caso 1

#Se defienen las condiciones para el caso con alpha = 1.3
h=0.09 #Se realiza un cambio de delta t al no conseguir convergencia con delta t = 0.1
N=int(T/h) # Nuevos arreglos con el nuevo delta t
alpha=1.3
a_euler=np.zeros(N)
m_euler=np.zeros(N)

a_euler[0]=0.4
m_euler[0]=0.3

me() #
s=1-(a_euler+m_euler) 

#Algoritmo que busca los maximos relativos de 's', en este caso se agrega la condicion de s[j]>0.1 debido a encontrar 'maximos falsos'
#Al encontrar un maximo, lo resta con el maximo anterior para luego agregarlo a una lista.
u=0  #Arreglo inicial para comenzar el algoritmo
frec1=[] #Lista que recopilara los periodos de los maximos
for j in range(1,N-1): #Algortimo que busca los maximos relativos de 's', en este caso se agrega la condicion de s[j]>0.1
    if s[j-1]<s[j] and s[j]>s[j+1]:  
        if s[j]>0.01:
            frec1.append((j-u)*h)
            u=j

#Caso 2

#Se defienen las condiciones para el caso con alpha = 1.4
#Se vuelve a trabajar con delta t = 0.1 y se realizan sus respectivos arreglos
h=0.1
N=int(T/h)
alpha=1.4
a_euler=np.zeros(N)
m_euler=np.zeros(N)

a_euler[0]=0.4
m_euler[0]=0.3

me()
s=1-(a_euler+m_euler) 
#Algoritmo que busca los maximos relativos de 's'
u=0
frec2=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec2.append((j-u)*h)
        u=j

#Caso 3

#Se defienen las condiciones para el caso con alpha = 1.5
alpha=1.5
me()
s=1-(a_euler+m_euler) 

#Algoritmo que busca los maximos relativos de 's'
u=0
frec3=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec3.append((j-u)*h)
        u=j
            
#Caso 4

#Se defienen las condiciones para el caso con alpha = 1.6
alpha=1.6
me()
s=1-(a_euler+m_euler) 
u=0
frec4=[]
#Algoritmo que busca los maximos relativos de 's'
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec4.append((j-u)*h)
        u=j       
        
#Caso 5

#Se defienen las condiciones para el caso con alpha = 1.7
alpha=1.7
me()
s=1-(a_euler+m_euler) 
#Algoritmo que busca los maximos relativos de 's'
u=0
frec5=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec5.append((j-u)*h)
        u=j 

#Caso 6

#Se defienen las condiciones para el caso con alpha = 1.8
alpha=1.8
me()
s=1-(a_euler+m_euler) 
#Algoritmo que busca los maximos relativos de 's'
u=0
frec6=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec6.append((j-u)*h)
        u=j 

#Caso 7

#Se defienen las condiciones para el caso con alpha = 1.9
alpha=1.9
me()
s=1-(a_euler+m_euler) 
#Algoritmo que busca los maximos relativos de 's'
u=0
frec7=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec7.append((j-u)*h)
        u=j         

#Se crea una lista que recopile los ultimos periodos de cada caso (periodo limite)
#Esta lista sera lista1_frec, se ocupara un '1' ya que con el transcurso del trabajo se haran mas listas parecidas
lista1_frec=[frec1[-1],frec2[-1],frec3[-1],frec4[-1],frec5[-1],frec6[-1],frec7[-1],]

#Se grafica los valores del periodo limite con respecto a alpha
fig = plt.figure(figsize=(8,6))
alph=np.arange(1.3,2,.1)  #arreglo de un intervalo [1.3,1.9]
plt.plot(alph,lista1_frec,'-')

#Se agrega el titulo y las etiquetas de los ejes
plt.title('Frecuencia de la formación de estrellas con Euler P. (c/r a Alpha)',fontsize=14) 
plt.ylabel('Periodo límite (millones de años)') 
plt.xlabel('Alpha variable')

