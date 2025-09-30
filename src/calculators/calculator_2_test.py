from typing import List
from typing import Dict
from .calculator_2 import Calculator2
from src.drivers.numpay_handler import NumpayHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self,body: Dict)  -> None:
        self.json = body

class MockDriverHandler:
    def standard_derivation(self, numbers: List) -> float:
        return 3
    
    def variance(self, numbers: List) -> float:
        return 3

# Integração entre NumpayHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [3.14, 2.67, 1.56] })
    
    driver = NumpayHandler()
    calculator_2 = Calculator2(driver)    
    formated_response = calculator_2.calculate(mock_request)

    
    assert isinstance(formated_response, dict)
    assert formated_response == {'data':{'Calculator': 2, 'result': 0.17}}

def test_calculate():
    mock_request = MockRequest({ "numbers": [3.14, 2.67, 1.56] })
    
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)    
    formated_response = calculator_2.calculate(mock_request)

    
    assert isinstance(formated_response, dict)
    assert formated_response == {'data':{'Calculator': 2, 'result': 0.33}}