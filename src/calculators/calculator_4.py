from flask import request as FlaskRequest
from typing import List, Dict
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> dict: # type: ignore
        body = request.json
        input_data = self.__validade_body(body)

        mean = self.__calculate_mean(input_data)
        formatted_response = self.__format_response(mean)
        return formatted_response
    
    def __validade_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
    
        input_data = body["numbers"]
        return input_data
    
    def __calculate_mean(self, numbers: List[float]) -> float:
        mean = self.__driver_handler.mean(numbers)
        return mean
    
    def __format_response(self, mean : float) -> dict:
        return{
            "data":{
                "Calculator": 4,
                "value": mean,
                "Success": True
            }
        }