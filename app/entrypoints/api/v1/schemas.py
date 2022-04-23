from pydantic import BaseModel, validator
from typing import List

import numpy as np


class Input(BaseModel):
    values: np.ndarray

    @validator("values", pre=True)
    def parse_values(v):
        return np.array(v, dtype=float)

    class Config:
        arbitrary_types_allowed = True
