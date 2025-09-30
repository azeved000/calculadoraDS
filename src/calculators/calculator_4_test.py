import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.calculators.calculator_4 import Calculator4
from typing import List, Dict


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def mean(self, numbers: List) -> float:
        return 22.0

def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 100] })
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {"data":{"Calculator": 4,"value": 22.0,"Success": True}}
    print()
    print(response)

