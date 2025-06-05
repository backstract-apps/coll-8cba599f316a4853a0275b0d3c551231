from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Addresses(BaseModel):
    id: int
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    created_at: datetime.time
    updated_at: datetime.time


class ReadAddresses(BaseModel):
    id: int
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True


class Persons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str
    to_be_deleted: int


class ReadPersons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str
    to_be_deleted: int
    class Config:
        from_attributes = True


class HelloasTesting(BaseModel):
    id: int


class ReadHelloasTesting(BaseModel):
    id: int
    class Config:
        from_attributes = True


class TestingTempo(BaseModel):
    id: int


class ReadTestingTempo(BaseModel):
    id: int
    class Config:
        from_attributes = True




class PostTesting(BaseModel):
    number_pages: int
    street_name: str
    offset_value: int

    class Config:
        from_attributes = True

