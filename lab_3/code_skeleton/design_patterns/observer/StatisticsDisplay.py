from numpy import maximum, minimum

from Observer import Observer
from DisplayElement import DisplayElement
from Observable import Observable

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self):
        self.__temperatures = []

    def update(self, observable: Observable):
        measurements = observable.get_measurements()

        self.__temperatures.append(measurements.temperature)

        self.display()

    def display(self):
        average = sum(self.__temperatures) / len(self.__temperatures)
        maximum = max(self.__temperatures)
        minimum = min(self.__temperatures)

        print(
        f"Avg/Max/Min temperature = "
        f"{average:.1f}/{maximum:.1f}/{minimum:.1f}"
    )

