from .PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.dough.ThickCrustDough import ThickCrustDough
from ingredients.sauce.PlumTomatoSauce import PlumTomatoSauce
from ingredients.cheese.Mozzarella import Mozzarella
from ingredients.veggies.BlackOlives import BlackOlives
from ingredients.veggies.Spinach import Spinach
from ingredients.veggies.EggPlant import EggPlant
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.clams.FrozenClams import FrozenClams

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return Mozzarella()

    def create_veggies(self):
        return [BlackOlives(), Spinach(), EggPlant()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()
