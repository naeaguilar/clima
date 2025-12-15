# oop_weather.py

class WeatherData:
    """
    Clase  para representar datos del clima.
    Encapsula una lista de temperaturas con atributos privados.
    """
    def __init__(self):
        self._temperaturas = []  # Atributo privado para encapsulamiento
    
    def agregar_temperatura(self, temperatura):
        """
        Método para agregar una temperatura a la lista.
        Valida que sea un número flotante.
        """
        if isinstance(temperatura, (int, float)):
            self._temperaturas.append(float(temperatura))
        else:
            raise ValueError("La temperatura debe ser un número.")
    
    def obtener_temperaturas(self):
        """
        Método para obtener la lista de temperaturas (acceso controlado).
        """
        return self._temperaturas.copy()  # Retorna una copia para evitar modificaciones externas
    
    def display_info(self):
        """
        Método polimórfico para mostrar información general.
        Puede ser sobrescrito en subclases.
        """
        print(f"Temperaturas registradas: {self._temperaturas}")

class WeeklyWeather(WeatherData):
    """
    Clase derivada de WeatherData para manejar el clima semanal.
    Hereda la funcionalidad base y agrega cálculo de promedio semanal.
    """
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase base
        self._dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    def ingresar_temperaturas_diarias(self):
        """
        Método para ingresar temperaturas diarias interactivamente.
        Solicita al usuario una temperatura por día.
        """
        for dia in self._dias_semana:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para {dia}: "))
                    self.agregar_temperatura(temp)  # Usar método heredado
                    break
                except ValueError as e:
                    print(f"Error: {e}. Intente nuevamente.")
    
    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal.
        Retorna el promedio como flotante.
        """
        temps = self.obtener_temperaturas()  # Acceso controlado
        if not temps:
            return 0.0
        return sum(temps) / len(temps)
    
    def display_info(self):
        """
        Sobrescribe el método de la clase base para mostrar información específica del clima semanal.
        """
        super().display_info()  # Llamar al método de la base
        promedio = self.calcular_promedio_semanal()
        print(f"Promedio semanal: {promedio:.2f} grados.")

def main():
    """
    Función principal para ejecutar el programa POO.
    Crea una instancia de WeeklyWeather y maneja el flujo.
    """
    print("Bienvenido al programa de cálculo del promedio semanal del clima (POO).")
    clima_semanal = WeeklyWeather()  # Instanciar objeto
    clima_semanal.ingresar_temperaturas_diarias()  # Ingresar datos
    clima_semanal.display_info()  # Mostrar resultados

# Ejecutar el programa si se corre directamente
if __name__ == "__main__":
    main()
