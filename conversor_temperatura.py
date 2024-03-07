while True:
    temperatura = float(input("Ingresa la temperatura deseada: "))
    unidad = input("Ingresa la unidad de medida(C. para Celsius, F. para Fahrenheit): ")

    if unidad == "C" or unidad == 'c' :
        fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
    elif unidad == "F" or unidad == 'f':
        celsius = (temperatura - 32) * 5/9
        print(f"{temperatura} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")
    else:
        print("Unidad de medida inválida. Inténtalo de nuevo.")

    opcion = input("Presiona 'C' para convertir otra temperatura, o 'F' para finalizar: ")
    if opcion == "F":
        break