from src.calculators.calculator_2 import Calculator2
from src.drivers.numpay_handler import NumpayHandler

def calculator2_factory():
    numpy_handler = NumpayHandler()
    calc = Calculator2(numpy_handler)
    return calc