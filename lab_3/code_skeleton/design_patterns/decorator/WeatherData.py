from IWeatherData import IWeatherData
from Observable import Observable
from Observer import Observer
from WeatherDataMeasurements import WeatherDataMeasurements
from ObservableWeatherData import ObservableWeatherData

class WeatherData(ObservableWeatherData):
    def __init__(self):
        self.__observers = []
        self.__measurements = None

    def register_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)

    def set_measurements(self, measurements: WeatherDataMeasurements):
        self.__measurements = measurements
        self.notify_observers()

    def get_measurements(self) -> WeatherDataMeasurements|None:
        return self.__measurements


