from typing import List, Optional
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    name: str 
    director: str 
    gender: List[str]
    shop: int
    rent: bool

class MovieRequestCreate(BaseModel):
    name: str
    director: str
    gender: List[str]
    shop: int

class MovieRequestUpdate(BaseModel):
    name: str
    director: str
    gender: List[str]

class MovieRequestUpdateShop(BaseModel):  
    shop: int

class Shop(BaseModel):
    id: int
    address: str
    manager: str 
    movies: List[Movie]

class ShopRequestCreate(BaseModel):
    address: str 
    manager: str 


class ShopUpdate(BaseModel):
    address: str 
    manager: str
