#Coding: utf-8
print("Tipos de Gasolina")
print("Super:")
print("Normal: 1.50€")
print("Turbo: 1.55€")
print("Sin Plomo")
print("Normal: 1.60€")
print("Con Aditivos(sabor naranja): 1.65€")
print("Diesel:")
print("Normal: 1.70€")
print("Fast&Furius: 1.75€")
super_normal=1
super_turbo=2
plomo_normal=3
plomo_conaditivos=4
diesel_normal=5
diesel_fastfurius=6
precio1=1.50
precio2=1.55
precio3=1.60
precio4=1.65
precio5=1.70
precio6=1.75
selecciona=int(input("Dime cuanta gasolina necessita: "))
litros=int(input("¿Cuantos litros necessita? "))
if(seleccion==1):
    resultado=(litros*precio1)
    print("Importe:", resultado,"€")
else:
    if(selecciona==2):
        resultado=(litros*precio2)
        print("Importe:", resultado,"€")
    else:
        if(selecciona==3):
            resultado=(litros*precio3)
            print("Importe:", resultado,"€")
        else:
            if(selecciona==4):
                resultado=(litros*precio4)
                print("Importe:", resultado,"€")
            else:
                if(selecciona==5):
                    resultado=(litros*precio5)
                    print("Importe:", resultado,"€")
                else:
                    if(selecciona==6):
                        resultado=(litros*precio6)
print("Importe:", resultado,"€")
