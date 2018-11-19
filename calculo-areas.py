#Coding: utf-8
print("Dime una figura geométrica:")
area=input("¿Qué figura quiere calcular (Escriba T o C)?")
if (area == "T"):
    altura=float(input("Dime la altura:"))
    base=float(input("Dime la base:"))
    respuesta=(base*altura/2)
    print("El triangulo tiene una area de",respuesta)
else:
    if (area == "C"):
        radio=float(input("Dime el radio:"))
        respuesta=(3.14*radio**2)
    print("El circulo tiene una area de",respuesta)
