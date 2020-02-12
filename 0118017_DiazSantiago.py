# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:08:45 2020

@author: Sachi
"""

#Santiago Dïaz Ruiz
#0118017
#Grupo 5 (miercolés y jueves)

#%% EJ1

while True:
    try:
        n = float(input('Digite un valor númerico cualquiera: ')) #entero o decimal
        if n>0 or n<0: break
        else:
            print('No fue ingresado un valor númerico')
    except:
        print('No fue ingresado un valor númerico')

if n >= 0:
    print ('EL valor alsoluto del número digitado es: ',n) #se imprime el número como está
elif n < 0:
    print ('EL valor alsoluto del número digitado es: ',n * -1) #se imprime multiplicado por -1

#%% EJ2
numero1 = int(input('Digite el primer número: '))
numero2 = int(input('Digite el segundo número: '))
numero = numero1 - numero2
print('La diferencia entre el primero y el segundo número es de ',numero)
val = range(2,numero)
contador = 0
for x in val:
    if numero % x == 0:
        contador += 1
if contador > 0:
    print('El número ',numero,' no es primo')
else:
    print('EL número ',numero,' es primo')

#%% EJ3

def multiplo(valor, multiplo):
    resto = valor % multiplo
    if resto == 0:
        return True
    else:
        return False
 
multiplos_3 = [0]
multiplos_4 = [0]

 
# para evaluar los cien primeros enteros positivos
for i in range(1,101):
 
    if multiplo(i,3):
        multiplos_3.append(i)
 
    if multiplo(i,4):
        multiplos_4.append(i)
 
print ("Los 15 primeros múltiplos de 3 son:", multiplos_3[0:15])
print ("Los múltiplos de 4 son:", multiplos_4)

#%% EJ4

import math as mt
input('Ingrese las coordenadas x,y y el radio r del primer \
círculo a continuación') 
x1 = float(input('Coordenada x: '))
y1 = float(input('Coordenada y: '))
r1 = float(input('Radio: '))
print(x1,y1,r1)

input('Ingrese las coordenadas x,y y el radio r del segundo \
círculo a continuación')
x2 = float(input('Coordenada x:'))
y2 = float(input('Coordenada y: '))
r2 = float(input('Radio:  '))
print(x2,y2,r2)

input('Ahora ingrese las coordenadas del punto que quiera evaluar, para \
saber en qué lugar se encuentra con respecto a los círculos')
a = float(input('Coordenada x:'))
b = float(input('Coordenada y: '))
k1 = mt.sqrt(((a-x1)**2 + (b-y1)**2))
k2 = mt.sqrt(((a-x2)**2 + (b-y2)**2))

if k1 <= r1 and k2 > r2:
    print('El punto se encuentra dentro del circulo 1')
if k2 <= r2 and k1 >= r1:
    print('EEl punto se encuentra dentro del circulo 2')
if k1 > r1 and k2 > r2:
    print('Está fuera de ambos circulos')
if k1 <= r1 and k2 <= r2:
    print(' Está dentro de ambos circulos')

#%% EJ5
    
def leer_frase():
    global txt
    txt = (input('Ingrese una cadena de texto: '))
    
def contar_vocales():
    vocal_Mayus = ['A','E','I','O','U','Á','É','Í','Ó','Ú']
    cont_vocM = 0
    for i in vocal_Mayus:
        for j in txt:
            if (i == j):
                cont_vocM += 1
    print('Hay ',cont_vocM,' vocales mayúsculas en la cadena de texto \
ingresada')
    
def contar_tildes():
    letras_tildes = ['Á','á','É','é','Í','í','Ó','ó','Ú','ú']
    cont_letT = 0
    for i in letras_tildes:
        for j in txt:
            if (i == j):
                cont_letT += 1
    print('Hay ',cont_letT,' letras tildadas en la cadena de texto ingresada')

def contar_digitos():
    digitos = ['1','2','3','4','5','6','7','8','9','0']
    cont_dig = 0
    for i in digitos:
        for j in txt:
            if (i == j):
                cont_dig += 1
    print('Hay ',cont_dig,' dígitos en la cadena de texto ingresada')
  
def contar_espacios():
    espacios = [' ']
    cont_esp = 0
    for i in espacios:
        for j in txt:
            if (i == j):
                cont_esp += 1
    print('Hay ',cont_esp,' espacios en la cadena de texto ingresada')

def contar_reserv():
    palabras = ['and','And','del','Del','for','For','is','Is','raise','Raise',
                'assert','Assert','if','If','else','Else','elif','Elif','from',
                'From','lamda','Lambda','return','Return','break','Break',
                'global','Global','not','Not','try','Try','class','Class',
                'except','Except','or','Or','while','While','continue',
                'Continue','exec','Exec','import','Import','yield','Yield',
                'def','Def','finally','Finally','in','In','print','Print']
    cont_pal = 0
    for i in palabras:
        for j in txt:
            if (i == j):
                cont_pal += 1
    print('Hay ',cont_pal,' palabras reservadas en la cadena de texto \
ingresada')

leer_frase()
contar_vocales()
contar_tildes()
contar_digitos()
contar_espacios()
contar_reserv()

#%% EJ6

def leer_frase():
    global x
    x = (input('Digite una frase: '))
    x = x.replace(' ', '')
    x = sorted(x) 
    x = ''.join(x)
 
leer_frase()
print(x)

#%% EJ7

x = eval(input('Escriba una lista ordenada de manera ascendente: '))
y = 0
z = 0
w = x[0] 

for i in x[1:len(x)+1]:
    if w > i:
        c = z
        print('Debo organizar la lista')
        break
    w = x[y+1]  
    y = y+1
    
if z == 0:
    h=-1
    x1 = float(input('ingresar numero: '))
    for i in x:  
        h=h+1
        if x1<=i: 
            x1.insert(h,x1)
            break
        if h==(len(x)-1):
            x.append(x1)
            break
            
print(x)

#%% EJ8

x = eval(input('ingrese una lista: '))
t = x[0]
g = 0

for i in x[1:len(x)+1]:
    g = g+1
    if t<i:
        t==i
        
x.remove(t)
t = x[0]
for i in x[1:len(x)+1]:
    g = g+1
    if t<i:
        t = i
        
print('el segundo número de mayor tamaño es ',t) 

#%% EJ9

numero = int(input('Dígame el valor de U(0): '))
valor = numero

while(valor > 1):
    if(valor % 2 == 0):
        valor = (valor / 2)
        print(str(valor)+ ' ')
        
    else:
        valor = (valor * 3) + 1
        print( str(valor)+' ')
        
#%% EJ10
        
M = [] # vector vacío

filas = int(input('Ingrese el número de filas de la matriz: '))
columnas = int(input('Ingrese el número de columnas de la matriz: '))

for i in range(filas): 
    M.append([]) #Se añade []
    for j in range(columnas):
        M[i].append(int(input(f'Escriba el elemento #{j+1} de la fila {i+1}: \
         '))) #Se agrega el valor ingresado a la sublista correspondiente

num_elementos = filas*columnas #Cantidad de elementos de la matriz
vec = []
col_final = columnas-1
col_inicial = 0
fil_final = filas-1
fil_inicial = 0
cont=0

while cont < num_elementos: 
    for i in range(col_final,col_inicial,-1): 
        pos = M[fil_final][i] 
        vec.append(pos)
        cont +=1 
    
    for i in range(fil_final,fil_inicial,-1):
        pos = M[i][col_inicial]
        vec.append(pos)
        cont +=1 

    for i in range(col_inicial,col_final):#
        pos = M[fil_inicial][i]
        vec.append(pos)
        cont +=1 
    
    for i in range(fil_inicial,fil_final):
        pos = M[i][col_final]
        vec.append(pos)
        cont +=1
    
    col_final -= 1
    col_inicial += 1
    fil_final = filas - 1
    fil_inicial += 1

print(vec)

#%% EJ11
    
def rectangulo(ancho, alto, letra):
    for i in range(alto):
        for j in range(ancho):
            print(letra, end = ' ')
        print()

anchura = int(input('Ancho del rectángulo: '))
altura = int(input('Alto del rectángulo: '))
caracter = input('Carácter a utilizar: ')

rectangulo(anchura, altura, caracter)

#%% EJ12

def creciente(ancho):
    for i in range(1, ancho + 1):
        for j in range(i):
            print('* ', end='')
        print()

def decreciente(ancho):
    for i in range(1, ancho):
        for j in range(ancho - i):
            print('* ', end='')
        print()

anchura = int(input('Anchura del triángulo: '))
creciente(anchura)
decreciente(anchura)

#%% EJ13

def num_bis(b):
    'Define la función que identifica si el año es bisiesto'
    return b % 400 == 0 or (b % 100 != 0 and b % 4 == 0)

print('Contador de años')
primer_año = int(input('Escriba un año: ')) #primer año del contador
print('Escriba otro año posterior a', str(primer_año) + ': ')
segun_año = int(input()) #siguiente año del contador
while segun_año < primer_año: #primer año mayor que el segundo
    print(segun_año,' no es mayor que ',str(primer_año),'. Inténtelo de nuevo:')
    segun_año = int(input())

año_bisiestos = 0 #años bisiestos
for x in range(primer_año, segun_año + 1):
    if num_bis(x):
        año_bisiestos += 1 #sumar 1 a la función si esta da año bisiesto
    
print('De ',primer_año,' a ',segun_año,' hay ',segun_año - primer_año + 1,
      ' años, ',año_bisiestos, 'de ellos bisiestos.')

#%% EJ14

import random as ran #número aleatorio
print('Escriba el resultado de las siguientes operaciones: ')

def fun():
    cont = 0     
    while cont<5: 
        a = ran.randint(1,100) 
        b = ran.randint(1,100) 
        c = a+b 
        d = int(input(f'{a} + {b} = ')) 
        
        if d == c:
            print('Respuesta correcta!')
            cont +=1
        else:
            print('Respuesta incorrecta!')
    print('Programa terminado')
fun()

#%% EJ15

import random as ran 

long = int(input('Dígame la longitud de la cadena: ')) 

def funcion(): 
    contador_intentos=0 
    num1 ='' 
    if long>=2 and long<=9: 
        for i in range(long):
            a = ran.randint(0,9) 
            num = str(a)  
            num1 = num1 + num  
       print(num1)
        
        usuario = input('Intente adivinar la cadena: ') 
        contador_intentos += 1 
        len_usuario = len(usuario) 
        while  len_usuario != long: 
            usuario = input('La longitud de la cadena ingresada es diferente a\
la inicial. Intenete adivinar la cadena: ')
            len_usuario = len(usuario) 
        aciertos = 0 
        while aciertos < long: 
            aciertos=0
            for j in range(long): 
                if num1[j] == usuario[j]: 
                    aciertos = aciertos + 1 
                    
                print(f'Con {usuario} ha adivinado {aciertos} valores. Felicid\
ades')
                print('Numero de intentos: ',contador_intentos)
                break  
            else:
                usuario = input(f'Con {usuario} ha adivinado {aciertos} valore\
s. Intente adivinar la cadena: ') 
                contador_intentos += 1 
                len_usuario = len(usuario)  
                while  len_usuario != long:
                    
                    usuario = input('La longitud de la cadena ingresada es dif\
erente a la inicial. Intenete adivinar la cadena: ') 
                    len_usuario = len(usuario)
    else:
        print('La longitud de cadena ingresada no se encuentra dentro del para\
metro del ejercicio.')
funcion()
#%%
    