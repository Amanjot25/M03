#Lee un número del teclado
#Si es par: Escribe “Qué bonito número par”
#Si es impar: Escribe “Qué número más vulgar”
#Pista: usar módulo %
#Juego de pruebas:
#Entrada        #Sortida
#   0          par i cero
#   2             par
#   5			       impar
#   7		         impar
#  -3			   impar i Negativo
#  -4			    par i Negativo

#Negativo, cero, par, impar

#Coding: utf-8
numero=int(input("Introduce un numero:"))
if(numero%2==0):
 print("Qué bonito",numero,"par")
else:
 print("Qué",numero,"más vulgar")
if (numero < 0):
    print("Negativo")
elif (numero == 0):
    print("Cero")
    
    
