#Coding: utf-8
print("Dime una figura geométrica:")
area=input("¿Qué figura quiere calcular (Escriba T o C)?")
if (area == "T"):
    altura=int(input("Dime la altura:"))
    base=int(input("Dime la base:"))
    respuesta=(base*altura/2)
    print("El triangulo tiene una area de",respuesta)
else:
    if (area == "C"):
        radio=int(input("Dime el radio:"))
        respuesta=(3.14*radio**2)
    print("El circulo tiene una area de",respuesta)
