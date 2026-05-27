
#nombre: Liceth Daniela Tarazona Plata
#grupo: 213022_305
#programa: Fundamentos de programación
#código de fuente: Autoría propia


# Matriz de inventario
inventario = [
    [101, "Teclado", 8, 15],
    [102, "Mouse", 20, 10],
    [103, "Monitor", 5, 8],
    [104, "Memoria USB", 12, 12],
    [105, "Impresora", 2, 6]
]

# Función para calcular cantidad a solicitar
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


# Recorrer la matriz
for articulo in inventario:

    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultados
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a solicitar:", pedido)
    print("------------------------")