
# Este es un archivo de prueba, sin actividades =) .

# A partir del próximo módulo: M03_variablesydatos vas a tener actividades para realizar.

#print('Hola Mundo!')
#a = 20
#while a > 0:
#    print(a)
#    a -= 1"


menu = {
    "BAJA TACO": 4.00,
    "BURRITO": 7.50,
    "BOWL": 8.50,
    "NACHOS": 11.00,
    "QUESADILLA": 8.50,
    "SUPER BURRITO": 8.50,
    "SUPER QUESADILLA": 9.50,
    "TACO": 3.00,
    "TORTILLA SALAD": 8.00
}

order_total = 0.0
lista= []
total=0
try:
    while True:
        item = input("Ingrese un artículo de su pedido o escriba 'listo' para finalizar: ").strip().upper()
        
        if item in menu:
            order_total += menu[item]
            lista.append(item)
            total+=1
        else:
            print("El artículo ingresado no está en el menú. Por favor, elija un artículo válido.")
except EOFError:
    print(f"Ud pidió {total} artículos. Estos son: {lista}. El total de la orden es: ${order_total:.2f}")