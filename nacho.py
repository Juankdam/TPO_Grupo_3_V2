# Declaración de la matriz global
matriz = [
    ["Nombre", "Apellido", "Cargo", "Empresa", "Teléfono", "Mail", "Cantidad de Productos Comprados", "Valor Total"],
    ["Juan", "Pérez", "Gerente", "Tech", "112", "@hola", "2", "10000"],
    ["María", "Martínez", "Asistente", "Coca", "100", "@chau", "5", "30"],
]

def promedio_valor_total(matriz):
    total_valor = 0
    cantidad_filas = 0

    # Itera sobre las filas de la matriz, ignorando la primera fila (encabezados)
    for fila in matriz[1:]:
        if len(fila) > 7:  # Asegúrate de que la fila tiene al menos 8 elementos
            total_valor += int(fila[7])  # Columna "Valor Total" (índice 7)
            cantidad_filas += 1
        else:
            print(f"Fila con datos insuficientes: {fila}")

    if cantidad_filas == 0:
        return 0  # Evitar división por cero

    promedio = total_valor / cantidad_filas
    return promedio

# Llamada a la función y mostrar el resultado
def main():
    promedio = promedio_valor_total(matriz)
    print(f"El promedio de la columna 'Valor Total' es: {promedio}")

if __name__ == "__main__":
    main()
