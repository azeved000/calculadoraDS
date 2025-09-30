from calculators.calculator_4 import Calculator4
from src.drivers.numpay_handler import NumpayHandler

def calculator4_factory():
    numpy_handler = NumpayHandler()
    calcu = Calculator4(numpy_handler)
    return calcu
