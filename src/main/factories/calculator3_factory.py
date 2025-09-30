from src.drivers.numpay_handler import NumpayHandler
from src.calculators.calculator_3 import Calculator3

def calculator3_factory():
    numpy_handler = NumpayHandler()
    calcu = Calculator3(numpy_handler)
    return calcu