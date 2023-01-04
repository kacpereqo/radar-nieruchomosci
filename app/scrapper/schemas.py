from pydantic import BaseModel


class Flat(BaseModel):
    title: str
    price: int
    area: float
    rooms: int
    floor: int
    is_rent: bool
    price_per_sqmeter: int
