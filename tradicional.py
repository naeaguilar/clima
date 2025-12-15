

def ingresar_temperaturas():
    """
    Ingresa las temperaturas diarias de la semana.
    Solicita al usuario ingresar una temperatura para cada día de la semana (7 días).
    Retorna una lista de temperaturas.
    """
    temperaturas = []  # Lista para almacenar las temperaturas
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    for dia in dias_semana:
        while True:  # Bucle para validar entrada numérica
            try:
                temp = float(input(f"Ingrese la temperatura para {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la temperatura.")
    
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio semanal de las temperaturas.
    Recibe una lista de temperaturas y retorna el promedio como flotante.
    """
    if not temperaturas:  # Validación para evitar división por cero
        return 0.0
    suma = sum(temperaturas)  # Suma de todas las temperaturas
    promedio = suma / len(temperaturas)  # Cálculo del promedio
    return promedio

def main():
    """
     organiza el flujo del programa.
    Llama a las funciones de entrada y cálculo, y muestra el resultado.
    """
    print("Hola,Bienvenido al programa de cálculo del promedio semanal del clima.")
    temperaturas = ingresar_temperaturas()  # Obtener datos del usuario
    promedio = calcular_promedio_semanal(temperaturas)  # Calcular promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")

# Ejecutar el programa si se corre directamente
if __name__ == "__main__":
    main()
