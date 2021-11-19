from pydantic import BaseModel, validator
from numpy import array, ndarray
from typing import List


class Input(BaseModel):
    values: ndarray

    @validator('values', pre=True)
    def parse_values(v):
        return array(v, dtype=float)

    class Config:
        arbitrary_types_allowed = True
