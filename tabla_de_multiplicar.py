#Crea un programa que solicite al usuario ingresar un número 
# entero positivo (N). El programa debe mostrar la tabla de
#multiplicar del número, teniendo en cuenta que se debe generar 
# la tabla con los primeros 10 valores de dicha tabla. 
# Solicitar al usuario que ingrese un número entero positivo (N)
Numero = int(input("Por favor, meta un número entero positivo  "))

if Numero > 0:
    for i in range(1, 11):
        print("{Numero} x {i} = {Numero * i}")
else:
    
    print("Debes ingresar un número entero positivo.")