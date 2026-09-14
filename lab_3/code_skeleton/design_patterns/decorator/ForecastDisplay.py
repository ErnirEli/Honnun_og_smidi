from Observer import Observer
from DisplayElement import DisplayElement
from Observable import Observable
from IWeatherData import IWeatherData

class ForecastDisplay(Observer, DisplayElement):

    def __init__(self):
        self.__last_pressure = 0
        self.__current_pressure = 0

    def update(self, observable: Observable):
        if isinstance(observable, IWeatherData):
            weather_data: IWeatherData = observable
            measurements = weather_data.get_measurements()

            self.__last_pressure = self.__current_pressure
            self.__current_pressure = measurements.pressure

            self.display()

    def display(self):
        if self.__current_pressure > self.__last_pressure:
            print("Forecast: Improving weather on the way!")

        elif self.__current_pressure < self.__last_pressure:
            print("Forecast: Watch out for cooler, rainy weather")

        else:
            print("Forecast: More of the same")
