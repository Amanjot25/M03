#Coding: utf-8
anyo=int(input("Dime un año : "))

if(anyo % 100 != 0):
    if(anyo % 4 == 0): 
       print ("Es bisiesto")
    else:
        print ("No es bisiesto")
        
elif(anyo % 400 == 0):
    print ("Es bisiesto")
    
else:
    print ("No es bisiesto")
