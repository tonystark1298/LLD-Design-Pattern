class Notes():
    def __init__(self) -> None:
        pass

    def is_available(self,val):
        return Two_Thousand_Notes().is_available(val)

class Two_Thousand_Notes(Notes):
    def __init__(self) -> None:
        pass
    def is_available(self,val):
        if(val%2000==0):
            return f"User get {val/2000} notes of 2000"
        else:
            return Five_Hundred_Notes().is_available(val)

class Five_Hundred_Notes(Notes):
    def __init__(self) -> None:
        pass
    def is_available(self,val):
        if((val%2000)%500==0):
            return f"User get {int(val/2000)} notes of 2000 and {int((val%2000)/500)} notes of 500"
        else:
            return Hundred_Notes().is_available(val)

class Hundred_Notes(Notes):
    def __init__(self) -> None:
        pass
    def is_available(self,val):
        if(((val%2000)%500)%100==0):
            return f"User get {int(val/2000)} notes of 2000 and {int((val%2000)/500)} notes of 500 and {int(((val%2000)%500)/100)} notes of 100"
        else:
            return f"Please Enter a Multiple of Hundred"
        
obj=Notes().is_available(2155)
print(obj)