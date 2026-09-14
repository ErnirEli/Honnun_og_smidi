from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'preparing: {self._name}')

        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._pepperoni = self._ingredient_factory.create_pepperoni()
