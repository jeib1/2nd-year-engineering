#Parte D
import numpy as np
import matplotlib.pyplot as plt

def f(a,m,t): #Se agrega una cordenada con 't' para el pasoRunge-Kutta
    f=1-a-m-k1*(m**2)*a  #Función que simula nuestra primera EDO; da/dt
    return f
def g(a,m,t): #Se agrega una cordenada con 't' para el paso Runge-Kutta
    g=k1*(m**2)*a-k2*(m**alpha)*(1-a-m)  #Función que simula nuestra segunda EDO; dm/dt
    return g

T=150  #El límite superior del intervalo para el periodo limte (en millones de años)
h=0.1 #Se define delta t
N=int(T/h) #Se define la cantidad de elementos del arreglo
k1=8 #Se define k1
k2=15 #Se define k2
t = np.arange(0,T+h,h) #Intervalo de tiempo [0,150] con el paso a 0.1
N = len(t) #Se define la cantidad de elementos del arreglo

# Se crea un ''lienzo en blanco'' para empezar a trabajar las funciones con el metodo Runge-Kutta
a_rk = np.zeros(N)
m_rk = np.zeros(N)

#Condiciones iniciales que no cambiaran si varia alpha
a_rk[0] = 0.4
m_rk[0] = 0.3

#Definimos el paso para el metodo de Runge Kutta
def rk(): #La funcion debe de dar el paso para 'a' como para 'm' por lo que se realizaran calculos para ambos a la vez 
    for i in range(N-1):
        g1a = h * f(a_rk[i], m_rk[i], t[i])
        g1m = h * g(a_rk[i], m_rk[i], t[i])
        g2a = h * f(a_rk[i] + g1a/2, m_rk[i] + g1m/2, t[i] + h/2)
        g2m = h * g(a_rk[i] + g1a/2, m_rk[i] + g1m/2, t[i] + h/2)
        g3a = h * f(a_rk[i] + g2a/2, m_rk[i] + g2m/2, t[i] + h/2)
        g3m = h * g(a_rk[i] + g2a/2, m_rk[i] + g2m/2, t[i] + h/2)
        g4a = h * f(a_rk[i] + g3a, m_rk[i] + g3m, t[i] + h)
        g4m = h * g(a_rk[i] + g3a, m_rk[i] + g3m, t[i] + h)
        a_rk[i + 1] = a_rk[i] + (1/6)*(g1a + 2*g2a + 2*g3a + 2*g4a)
        m_rk[i + 1] = m_rk[i] + (1/6)*(g1m + 2*g2m + 2*g3m + 2*g4m)

#Se busca el PERIODO LIMITE c/r a alpha 

#Caso 1
#Se defienen las condiciones para el caso con alpha = 1.3
alpha=1.3
rk() #Se pone a correr el metodo
s=1-(a_rk+m_rk) 
#Algoritmo que busca los maximos relativos de 's'
u=0
frec1=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        if s[j]>0.01: #En este caso se agrega la condicion de s[j]>0.1 para evitar falsos maximos
            frec1.append((j-u)*h)
            u=j

#Caso 2
#Se defienen las condiciones para el caso con alpha = 1.4
alpha=1.4
rk()
s=1-(a_rk+m_rk) 
u=0
frec2=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec2.append((j-u)*h)
        u=j

#Caso 3
#Se defienen las condiciones para el caso con alpha = 1.5
alpha=1.5
rk() #Se pone a correr el metodo
s=1-(a_rk+m_rk)  
u=0
frec3=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec3.append((j-u)*h)
        u=j
            
#Caso 4
#Se defienen las condiciones para el caso con alpha = 1.6
alpha=1.6
rk()
s=1-(a_rk+m_rk) 
u=0
frec4=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec4.append((j-u)*h)
        u=j       
        
#Caso 5
#Se defienen las condiciones para el caso con alpha = 1.7
alpha=1.7
rk() #Se pone a correr el metodo
s=1-(a_rk+m_rk) 
u=0
frec5=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec5.append((j-u)*h)
        u=j 

#Caso 6
#Se defienen las condiciones para el caso con alpha = 1.8
alpha=1.8
rk() #Se pone a correr el metodo
s=1-(a_rk+m_rk) 
u=0
frec6=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec6.append((j-u)*h)
        u=j 

#Caso 7
#Se defienen las condiciones para el caso con alpha = 1.9
alpha=1.9
rk() #Se pone a correr el metodo
s=1-(a_rk+m_rk) 
u=0
frec7=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec7.append((j-u)*h)
        u=j         

#Se crea una lista que recopile los ultimos periodos de cada caso (periodo limite)
#Esta lista es lista2 ya que lista1 esta para Euler Progresivo
lista2_frec=[frec1[-1],frec2[-1],frec3[-1],frec4[-1],frec5[-1],frec6[-1],frec7[-1],]

#Se grafica los valores del periodo limite con respecto a alpha
fig = plt.figure(figsize=(8,6))
alph=np.arange(1.3,2,.1)  #arreglo de un intervalo [1.3,1.9]
plt.plot(alph,lista2_frec,color="#ff7700")  #Color anaranjado
#Se agrega el titulo y las etiquetas de los ejes
plt.title('Frecuencia de la formación de estrellas con RK4 (c/r a Alpha)',fontsize=14) 
plt.ylabel('Periodo límite (millones de años)')
plt.xlabel('Alpha variable')

