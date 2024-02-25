class Super_Factory():
    def __init__(self) -> None:
        pass
    def production_capacity(self):
        pass
    def workers_count(self):
        pass
    def wheel_count(self):
        pass
    def acceleration(self):
        pass
    def is_luxurious(self):
        pass
class Normal_Factory_Cars(Super_Factory):
    def __init__(self) -> None:
        pass
        #super().__init__()
    def production_capacity(self):
        return 100
    def workers_count(self):
        return 10000
class Luxury_Factory_Cars(Super_Factory):
    def __init__(self) -> None:
        pass
        #super().__init__()
    def production_capacity(self):
        return 10
    def workers_count(self):
        return 5000
class BMW(Luxury_Factory_Cars):
    def __init__(self) -> None:
        pass
        #super().__init__()
    
    def wheel_count():
        return 4
    def acceleration(self):
        return "10 HP"
    def is_luxurious(self):
        "YES"
class Ferrari(Luxury_Factory_Cars):
    def __init__(self) -> None:
        pass
        #super().__init__()
    
    def wheel_count(self):
        return 4
    def acceleration(self):
        return "12 HP"
    def is_luxurious(self):
        "YES"
class Maruti(Normal_Factory_Cars):
    def __init__(self) -> None:
        pass
        #super().__init__()
    def wheel_count():
        return 4
    def acceleration(self):
        return "5 HP"
    def is_luxurious(self):
        "No"
class Bike_Yamaha(Normal_Factory_Cars):
    def __init__(self) -> None:
        pass
        #super().__init__()
    def wheel_count(self):
        return 2
    def acceleration(self):
        return "2 HP"
    def is_luxurious(self):
        "NO"

obj1=Normal_Factory_Cars()
print(obj1.production_capacity())
obj2=Luxury_Factory_Cars()
print(obj2.production_capacity())