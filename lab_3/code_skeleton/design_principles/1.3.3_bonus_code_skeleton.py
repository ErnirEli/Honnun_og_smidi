from dataclasses import dataclass
from enum import Enum
from typing import List
from abc import ABC, abstractmethod

class ShipmentType(Enum):
    plane = 0
    ship = 1
    car = 2
    carrier_pigeon = 3


@dataclass
class Size:
    width: float
    height: float
    weight: float


@dataclass
class Product:
    name: str
    price: float
    size: Size


@dataclass
class Address:
    country: str
    street_address: str
    city: str
    zip_code: int

    def __str__(self):
        return f'{self.street_address}, {self.zip_code} {self.city}, {self.country}'


@dataclass
class Person:
    name: str
    ssn: str
    address: Address


@dataclass
class Package:
    shipment_type: ShipmentType
    product: Product
    merchant: Person
    buyer: Person


class Ship:
    def reload_fuel_oil(self):
        print('reloading fuel supplies on ship')

    def ship(self, package: Package):
        print(f'shipping package via ship from {package.merchant.address} to {package.buyer.address}')


class Plane:
    def reload_jet_fuel(self):
        print('jet fuels can\'t melt steel beams')

    def fly(self, package: Package):
        print(f'flying package from {package.merchant.address} to {package.buyer.address}')


class Car:
    def reload_gas(self):
        print('adding gasoline... or diesel')

    def drive(self, package: Package):
        print(f'driving package from {package.merchant.address} to {package.buyer.address}')


class CarrierPigeon:
    def eat_seeds(self):
        print(f'beep beep I\'m a bird')

    def fly(self, package: Package):
        print(f'beep beep I\'m a bird')


class ShipmentMethod(ABC):
    @abstractmethod
    def ship(self, package: Package):
        pass

class ShipShipment(ShipmentMethod):
    def ship(self, package: Package):
        ship = Ship()
        ship.reload_fuel_oil()
        ship.ship(package)

class PlaneShipment(ShipmentMethod):
    def ship(self, package: Package):
        plane = Plane()
        plane.reload_jet_fuel()
        plane.fly(package)

class CarShipment(ShipmentMethod):
    def ship(self, package: Package):
        car = Car()
        car.reload_gas()
        car.drive(package)

class CarrierPigeonShipment(ShipmentMethod):
    def ship(self, package: Package):
        pigeon = CarrierPigeon()
        pigeon.eat_seeds()
        pigeon.fly(package)

class ShipmentService:
    def __init__(self):
        self.__shipment_methods = {
            ShipmentType.ship: ShipShipment(),
            ShipmentType.plane: PlaneShipment(),
            ShipmentType.car: CarShipment(),
            ShipmentType.carrier_pigeon: CarrierPigeonShipment()
        }

    def ship(self, package: Package):
        shipment_method = self.__shipment_methods[package.shipment_type]
        shipment_method.ship(package)


''' TEST CASES '''


if __name__ == "__main__":
    merchant = Person(
        "Merchant",
        "111",
        Address("Iceland", "Street 1", "Reykjavik", 101)
    )

    buyer = Person(
        "Buyer",
        "222",
        Address("Iceland", "Street 2", "Reykjavik", 105)
    )

    product = Product(
        "Laptop",
        250000,
        Size(30, 20, 2)
    )

    package = Package(
        ShipmentType.plane,
        product,
        merchant,
        buyer
    )

    shipment_service = ShipmentService()
    shipment_service.ship(package)



