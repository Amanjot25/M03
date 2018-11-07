#Coding: utf-8

print("AÑOS")
anyo_actual = int(input("El año actual es: "))
anyo_cualquiera = int(input("Dime un año cualquiera: "))
desigualdad = anyo_actual - anyo_cualquiera
if  desigualdad == 1:
    print("Desde el año,anyo_cualquiera,ha pasado 20 años")
elif desigualdad > 1:
    print("Desde el año,anyo_cualquiera,han pasado ,desigualdad, años")
elif desigualdad == -1:
    print("Para llegar al año ,anyo_cualquiera, falta 2 años")
elif desigualdad < -1:
    print("Para llegar al año ,anyo_cualquiera, faltan ,-desigualdad, años")
else:
    print("¡Son el mismo año!")
