from pydantic import BaseModel


class WclassBase(BaseModel):
    name: str


class WclassCreate(WclassBase):
    pass


class Wclass(WclassBase):
    id: int

    class Config:
        orm_mode = True


class GamemodeBase(BaseModel):
    name: str


class GamemodeCreate(GamemodeBase):
    name: str


class Gamemodes(GamemodeBase):
    id: int

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    name: str
    zip: int
    city: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int
    zip: int
    city: str

    class Config:
        orm_mode = True