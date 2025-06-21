"""
A pydantic dataclass is a way of representing a set of data in python. A dataclass contains the column names and type
in the form of a python model.
"""

from datetime import datetime

from pydantic import BaseModel


class Car(BaseModel):
    make: str
    date: datetime
    color: str
    engine: str
