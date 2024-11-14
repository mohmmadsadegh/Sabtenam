from abc import ABC,abstractmethod
class castoum(ABC):
    @abstractmethod
    def __init__(self):
        pass
    name=str
    famili=str             
class castoumFree(castoum):
    def __init__(self):
        self.freeCode=0
class castoumVIP(castoum):
    def __init__(self):
        self.personelCode=0    
castoum.name="hosi"  
castoumFree.name="sina" 
print(castoumFree.name) 
castoumVIP.name="sadegh"
print(castoumVIP.name)
castoumFree.freeCode=122
print(castoumFree.freeCode)
objcastoumNone=castoum()
objcastoumNone.name="heshmat"
print(objcastoumNone.name)
