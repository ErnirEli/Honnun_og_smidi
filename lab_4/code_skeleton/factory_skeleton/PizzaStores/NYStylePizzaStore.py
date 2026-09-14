from .PizzaStore import PizzaStore
from pizzas.PizzaType import PizzaType
from pizzas.CheesePizza import CheesePizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.ClamPizza import ClamPizza
from pizzas.VeggiePizza import VeggiePizza
from ingredient_factories.NYPizzaIngredientFactory import NYPizzaIngredientFactory

class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")

        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")

        elif pizza_type == PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")

        return pizza

