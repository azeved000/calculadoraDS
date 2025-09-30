import numpy
from typing import List

class NumpayHandler:
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return float(self.__np.std(numbers))
    
    # É como se fosse um gerente de biblioteca externa

    def variance(self,numbers: List[float]) -> float:
        return self.__np.var(numbers)
    
    def mean(self, numbers: List[float]) -> float:
        return float(self.__np.mean(numbers))