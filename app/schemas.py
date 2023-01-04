from pydantic import BaseModel


class WclassBase(BaseModel):
    class_name: str


class WclassCreate(WclassBase):
    pass


class Wclass(WclassBase):
    class_id: int

    class Config:
        orm_mode = True


class GamemodeBase(BaseModel):
    gamemode_name: str


class GamemodeCreate(GamemodeBase):
    pass


class Gamemodes(GamemodeBase):
    gamemode_id: int

    class Config:
        orm_mode = True


class GamemodeUpdate(BaseModel):
    gamemode_name: str


class LocationBase(BaseModel):
    location_name: str
    zip: int
    city: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    location_id: int

    class Config:
        orm_mode = True
