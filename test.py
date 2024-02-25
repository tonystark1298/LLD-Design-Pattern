class Base_Pizza():
    def __init__(self) -> None:
        pass
    def cost(self):
        pass

class Margheritta_Pizza(Base_Pizza):
    def __init__(self) -> None:
        pass
    def cost(self):
        return 100

class Veg_Delight_Pizza(Base_Pizza):
    def __init__(self) -> None:
        pass
    def cost(self):
        return 150

class Topping_Decorator():
    def __init__(self,base_pizza) -> None:
        self.base_pizza=base_pizza
        super().__init__()
    def cost(self):
        return self.base_pizza.cost()

class Extra_Cheese(Topping_Decorator):
    def __init__(self, base_pizza) -> None:
        self.base_pizza=base_pizza
        #super().__init__(base_pizza)
        pass
    def cost(self):
        return self.base_pizza.cost()+50
    
class Extra_Toppings(Topping_Decorator):
    def __init__(self, base_pizza) -> None:
        self.base_pizza=base_pizza
        #super().__init__(base_pizza)
        pass
    def cost(self):
        return self.base_pizza.cost()+100

obj1=Extra_Toppings(Extra_Cheese(Margheritta_Pizza())).cost()
print(obj1)
obj2=Extra_Cheese(Veg_Delight_Pizza()).cost()
print(obj2)
print("Base Pizza cost", Veg_Delight_Pizza().cost())