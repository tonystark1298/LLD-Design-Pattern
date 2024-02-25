#Pipeline Pattern
class get_data():
    def __init__(self,inst) -> None:
        self.inst=inst
        pass
    def get_val(self,given_data):
        data=given_data        
        for i in self.inst:
            data=i(data)
        return data

def process1(data):
    return data+10

def process2(data):
    return data*2

def process3(data):
    return data*5

obj=get_data([process1,process2,process3])
print(obj.get_val(1))