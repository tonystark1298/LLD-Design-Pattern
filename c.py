from datetime import datetime
class Parking_Manager():
    def __init__(self,wheel) -> None:
        self.wheel=wheel
    def entry_gate(self):  
        if(self.wheel==2):
            x=Two_Wheeler_Parking_Spot().is_empty()
            if(x):
                return ["Your Parking slot is ",x]
        else:
            if(Four_Wheeler_Parking_Spot().is_empty()):
                return f"Your Parking slot is {Four_Wheeler_Parking_Spot().is_empty()}"
    def get_cost(self,spot):
        if(self.wheel==2):
            x=Two_Wheeler_Parking_Spot().get_cost(spot)
            return ["cost",x]
                
        else:
            if(Four_Wheeler_Parking_Spot().get_cost(spot)):
                return f"cost is {Four_Wheeler_Parking_Spot().get_cost(spot)}"
        

class Parking_Spot():
    def __init__(self) -> None:
        pass
    def is_empty(self):
        pass
    def get_cost(self):
        pass

class Two_Wheeler_Parking_Spot(Parking_Spot):
    def __init__(self) -> None:
        pass
    def is_empty(self):
        for i in range (50,100):
            if(Spot(i).is_empty()):
                return i
        return False
    def get_cost(self,spot_id):
        return Spot(spot_id).get_cost()

class Four_Wheeler_Parking_Spot(Parking_Spot):
    def __init__(self) -> None:
        pass
    def is_empty(self):
        for i in range (0,50):
            if(Spot(i).is_empty()):
                return i
        return False
    def get_cost(self,spot_id):
        return Spot(spot_id).get_cost()

class Spot(Parking_Spot):
    dict_spot={}
    for i in range (0,101):
        dict_spot[i]=[]
    def __init__(self,no) -> None:
        self.no=no
        pass
    def is_empty(self):
        if(len(self.dict_spot[self.no])==0):
            s=str(datetime.now())
            s=""+s[11]+s[12]
            print(self.no)
            self.dict_spot[self.no]=s
            return True
    def get_cost(self):
            s=str(datetime.now())
            s=""+s[11]+s[12]
            print(s)
            print (self.dict_spot[self.no])
            rs=int(s)-int(self.dict_spot[self.no])
            self.dict_spot[self.no]=[]
            return rs
obj=Parking_Manager(2)
x=obj.entry_gate()[1]
print(x)
print(obj.get_cost(x))

