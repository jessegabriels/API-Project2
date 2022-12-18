from sqlalchemy import Column, Integer, String
from databse import Base


class Wclass(Base):
    __tablename__ = "class"

    class_id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, index=True)


class Gamemodes(Base):
    __tablename__ = "gamemodes"

    gamemode_id = Column(Integer, primary_key=True, index=True)
    gamemode_name = Column(String, index=True)


class Location(Base):
    __tablename__ = "location"

    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, index=True)
    zip = Column(Integer, index=True)
    city = Column(String, index=True)
