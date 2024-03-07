#Crea un programa que solicite al usuario ingresar valores
# y este debe verificar cuando se ingresa una vocal, el programa
#debe contar y mostrar la cantidad de vocales
# (a, e, i, o, u) ingresadas cuantas, de cada una y la cantidad total, importante
#tener en cuenta que la aplicación se detiene con una opción de menú llamada finalizar. 
contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
vocales= 0
while True:
    valor = input("ingresa una vocal o ingresa la palabra finalizar para salir ").lower()
    if valor == 'finalizar':
        break
    if valor in contador_vocales:
        contador_vocales[valor] += 1
total_vocales = sum(contador_vocales.values())
print("El número total de vocales ingresadas es .", total_vocales)
for vowel, count in contador_vocales.items():
    print(f"el numero {vocales} caracteres: {count}")