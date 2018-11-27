#Coding: utf-8
dividendo = int(input("Escribe el dividendo: "))
divisor = int(input("Escribe el divisor: "))

if divisor == 0:
    print("No puedes dividir por 0")
else:
    cociente= dividendo // divisor
    resto= dividendo % divisor
    if dividendo % divisor == 0:
        print("La división es exacta. cociente:" ,cociente ,"resto:" ,resto)
    else:
        print("La división no es exacta. cociente:" ,cociente ,"resto:" ,resto)
