from typing import Dict
from .http_unprocessable_entity import HttpUnprocessableEntity
from .http_bad_request import HttpBadRequest

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntity, HttpBadRequest)):
        return{
            "status_code": error.status_code,
            "body":{
                "errors": [{
                    "tittle": error.name,
                    "detail": error.message
                }]
            }
        }

    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "tittle": "Server Error",
                "detail": str(error)
            }]
        }
    }

