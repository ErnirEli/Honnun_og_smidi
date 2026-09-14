from ObservableWeatherData import ObservableWeatherData


class WeatherDataDecorator(ObservableWeatherData):
    def __init__(self, weather_data: ObservableWeatherData):
        self.__weather_data = weather_data
        self.__last_measurements = None

    def register_observer(self, observer):
        self.__weather_data.register_observer(observer)

    def remove_observer(self, observer):
        self.__weather_data.remove_observer(observer)

    def notify_observers(self):
        self.__weather_data.notify_observers()

    def get_measurements(self):
        return self.__weather_data.get_measurements()

    def set_measurements(self, measurements):
        if self.__last_measurements is None:
            self.__weather_data.set_measurements(measurements)
            self.__last_measurements = measurements
            return

        temp_change = abs(
            measurements.temperature - self.__last_measurements.temperature
        )

        humidity_change = abs(
            measurements.humidity - self.__last_measurements.humidity
        )

        pressure_change = abs(
            measurements.pressure - self.__last_measurements.pressure
        )

        if (
            temp_change >= 1
            or humidity_change >= 1
            or pressure_change >= 1
        ):
            self.__weather_data.set_measurements(measurements)
            self.__last_measurements = measurements