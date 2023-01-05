from pydantic import BaseModel
from typing import Optional


class Flat(BaseModel):
    price: int
    area: int
    rooms: int
    floor: int
    is_rent: bool
    is_furnished: Optional[bool]
    type_of_building: str
    owner: str
    url: str
    price_per_sqmeter: int
