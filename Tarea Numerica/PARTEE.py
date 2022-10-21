from scipy.integrate import odeint #Se importa SciPy y el modulo Odeint para el desarrollo
import numpy as np
import matplotlib.pyplot as plt

alpha=1.2
def odes(x,t): #Se definen las EDOS
    k1=8  #Constantes
    k2=15
        
    a=x[0]       #Define en un vector a y m
    m=x[1]
        
    dadt = 1-m-a-k1*(m**2)*a        #Simula da/dt
    dmdt = k1*(m**2)*a-k2*(m**alpha)*(1-m-a)     #Simula dm/dt
 
    return [dadt,dmdt]

x0 = [0.4,0.3]  #Condiciones iniciales
T=150    #El límite superior del intervalo para el periodo limte (en millones de años)
h=0.09  #Paso del tiempo que se usara para los tres metodos de ahora en adelante
N=int(T/h)

t = np.linspace(0,T,N)   #Arreglo de tiempo
x=odeint(odes, x0, t)      #Se ocupa odeint para resolver el sistema

a = x[:,0]   #Se valoriza a
m = x[:,1]   #Se valoriza m
s=1-(a+m)  #s con 1=a+m+s

#Se busca el PERIODO LIMITE c/r a alpha 

#Caso 1
alpha=1.3
x=odeint(odes, x0, t)

a = x[:,0]
m = x[:,1]
s=1-(a+m)
#Algoritmo que busca los maximos relativos de 's'
u=0
frec1=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        if s[j]>0.01:
           frec1.append((j-u)*h)
           u=j

#Caso 2
alpha=1.4
x=odeint(odes, x0, t)

a = x[:,0]
m = x[:,1]
s=1-(a+m)
#Algoritmo que busca los maximos relativos de 's'
u=0
frec2=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec2.append((j-u)*h)
        u=j

#Caso 3
alpha=1.5
x=odeint(odes, x0, t)

a = x[:,0]
m = x[:,1]
s=1-(a+m) 
#Algoritmo que busca los maximos relativos de 's'
u=0
frec3=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec3.append((j-u)*h)
        u=j
            
#Caso 4
alpha=1.6
x=odeint(odes, x0, t)

a = x[:,0]
m = x[:,1]
s=1-(a+m)
#Algoritmo que busca los maximos relativos de 's'
u=0
frec4=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec4.append((j-u)*h)
        u=j       
        
#Caso 5
alpha=1.7
x=odeint(odes, x0, t)

a = x[:,0]
m = x[:,1]
s=1-(a+m)
#Algoritmo que busca los maximos relativos de 's'
u=0
frec5=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec5.append((j-u)*h)
        u=j 

#Caso 6
alpha=1.8
x=odeint(odes, x0, t)

a = x[:,0]
m = x[:,1]
s=1-(a+m)
#Algoritmo que busca los maximos relativos de 's'
u=0
frec6=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec6.append((j-u)*h)
        u=j 

#Caso 7
alpha=1.9
x=odeint(odes, x0, t)

a = x[:,0]
m = x[:,1]
s=1-(a+m)

u=0
frec7=[]
for j in range(1,N-1):
    if s[j-1]<s[j] and s[j]>s[j+1]:
        frec7.append((j-u)*h)
        u=j         
#Se define la lista3 con los periodos limite de casa caso para la resolucion con odeint
lista3_frec=[frec1[-1],frec2[-1],frec3[-1],frec4[-1],frec5[-1],frec6[-1],frec7[-1],]

'''DESDE AQUI SE COPIARAN LA PARTE C Y D PARA CONSEGUIR SUS PERIODOS LIMITES'''
'''SE CONSIDERARA 'DELTA T' = 0.09 PARA TODOS LOS CASOS'''

'''PARTE C'''

def ec_1(x):
    return 1-x[0]-x[1]-k1*x[0]*(x[1]**2) #Función que simula nuestra primera EDO; da/dt
def ec_2(x):
    return k1*x[0]*(x[1])**(2)-k2*(x[1]**alpha)*(1-x[0]-x[1])  #Función que simula nuestra segunda EDO; dm/dt

def euler1(dt,x):
    return dt*ec_1(x)  #Computa al aproximación de Euler para la primera EDO
def euler2(dt,x):
    return dt*ec_2(x) #Computa al aproximación de Euler para la segunda EDO

T=150  #El límite superior del intervalo para el periodo limte (en millones de años)
h=0.09 #Se define delta t
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
h=0.09
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

'''PARTE D'''

def f(a,m,t): #Se agrega una cordenada con 't' para el pasoRunge-Kutta
    f=1-a-m-k1*(m**2)*a  #Función que simula nuestra primera EDO; da/dt
    return f
def g(a,m,t): #Se agrega una cordenada con 't' para el paso Runge-Kutta
    g=k1*(m**2)*a-k2*(m**alpha)*(1-a-m)  #Función que simula nuestra segunda EDO; dm/dt
    return g

T=150  #El límite superior del intervalo para el periodo limte (en millones de años)
h=0.09 #Se define delta t
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
lista2_frec=[frec1[-1],frec2[-1],frec3[-1],frec4[-1],frec5[-1],frec6[-1],frec7[-1],]

fig = plt.figure(figsize=(8,6))
alph=np.arange(1.3,2,0.1)

plt.plot(alph,lista1_frec,'-',label='Euler progresivo')
plt.plot(alph,lista2_frec,'-',label='Runge-Kutta 4')
plt.plot(alph,lista3_frec,'-',label='Scipy')

plt.title('Frecuencia de la formación de estrellas (c/r a Alpha)')
plt.legend(loc='upper right', fontsize=12)
plt.ylabel('Periodo límite (millones de años)')
plt.xlabel('Alpha variable')