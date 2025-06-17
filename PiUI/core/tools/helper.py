
from typing import Tuple

def enforceType(value, expected_types: Tuple, name: str):

    if not isinstance(value, expected_types):
        raise TypeError(
        f"\n{name} must be of type {[x.__name__ for x in expected_types]}. Got type: {type(value).__name__}"
        )
        
