class WeighingMachine():
    def __init__(self) -> None:
        pass
    def get_weight():
        pass
class WeightInKg(WeighingMachine):
    def __init__(self) -> None:
        pass
    def get_weight(self):
        return 100
class WeightFromKgToPound(WeighingMachine):
    def __init__(self,inst) -> None:
        self.inst=inst
        pass
    def get_weight(self):
        return 2*(self.inst().get_weight())
if __name__=="__main__":
    print(WeightFromKgToPound(WeightInKg).get_weight())