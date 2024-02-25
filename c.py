class Pizza_Director():
    def __init__(self) -> None:
        pass
    def get_extra_toppings_veg_delight(self):
        return Extra_Toppings(Veg_Delight_Pizza())
    def get_extra_toppings_margherita(self):
        return Extra_Toppings(Marghrita_Pizza())

class Base_Pizza():
    def __init__(self) -> None:
        pass
    def get_cost(self):
        pass

class Marghrita_Pizza(Base_Pizza):
    def __init__(self) -> None:
        pass
    def get_cost(self):
        return 100
    
class Veg_Delight_Pizza(Base_Pizza):
    def __init__(self) -> None:
        pass
    def get_cost(self):
        return 150
      
class Extra_Toppings(Base_Pizza):
    def __init__(self,inst) -> None:
        self.inst=inst
        pass
    def get_cost(self):
        return self.inst.get_cost()+50

print(Pizza_Director().get_extra_toppings_margherita().get_cost())