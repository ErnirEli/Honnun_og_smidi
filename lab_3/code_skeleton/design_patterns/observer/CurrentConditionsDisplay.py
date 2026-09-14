from Observer import Observer
from DisplayElement import DisplayElement
from Observable import Observable

class CurrentConditionsDisplay(Observer, DisplayElement):

    def update(self, observable: Observable):
        measurements = observable.get_measurements()

        self.__temperature = measurements.temperature
        self.__humidity = measurements.humidity

        self.display()

    def display(self):
        print(
        f"Current conditions: {self.__temperature:.1f}F degrees "
        f"and {self.__humidity:.1f}% humidity"
        )
