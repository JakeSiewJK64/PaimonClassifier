from pydantic import BaseModel, conlist
from typing import List

class MyData(BaseModel):
    data: List[List[int]]
