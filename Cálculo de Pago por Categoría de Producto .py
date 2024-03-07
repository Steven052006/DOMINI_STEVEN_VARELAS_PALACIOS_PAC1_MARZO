#Escribe un programa en Python que permita calcular el pago de
# un producto en una tienda, tomando en cuenta que los productos se encuentran
#clasificados en cinco categorías: Ferretería, Aseo, Seguridad, Alimentos y
#Electrodomésticos. Cada categoría tiene un descuento diferente aplicado al
#precio del producto, el cual debe presentar un menú de opciones donde solo
# se termina el sistema con la opción “TERMINAR”.
#Descuentos por Categoría: Ferretería: 10% Aseo: 5% Seguridad: 15% Alimentos:
# 8% Electrodomésticos: 12%
#El programa debe solicitar al usuario ingresar la categoría y el precio de 
# cada producto comprado, y luego calcular el precio final con el descuento
#aplicado. Al finalizar, debe mostrar la cantidad de productos comprados por 
# cada categoría y el total recaudado. 
descuentos = {
    "Ferretería": 0.10,
    "Aseo": 0.05,
    "Seguridad": 0.15,
    "Alimentos": 0.08,
    "Electrodomésticos": 0.12
}

cantidades = {
    "Ferretería": 0,
    "Aseo": 0,
    "Seguridad": 0,
    "Alimentos": 0,
    "Electrodomésticos": 0
}

total_recaudado = 0

opciones = {
    "1": "Ferretería",
    "2": "Aseo",
    "3": "Seguridad",
    "4": "Alimentos",
    "5": "Electrodomésticos",
    "6": "TERMINAR"
}

def calcular_precio_final(categoria, precio):
    descuento = descuentos[categoria]
    precio_final = precio * (1 - descuento)
    return precio_final

def mostrar_menu():
    print("Menú de opciones:")
    for opcion, categoria in opciones.items():
        print(f"{opcion}: {categoria}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "6":
            break
        categoria = opciones[opcion]
        precio = float(input(f"Ingrese el precio del producto {categoria}: "))
        precio_final = calcular_precio_final(categoria, precio)
        cantidades[categoria] += 1
        total_recaudado += precio_final
        print(f"El precio final del producto {categoria} es: {precio_final}")
        print()
    print("Resultados:")
    for categoria, cantidad in cantidades.items():
        print(f"{categoria}: {cantidad} productos")
    print(f"Total recaudado: {total_recaudado}")

if __name__ == "__main__":
    main()