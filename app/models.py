from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Wclass(Base):
    __tablename__ = "class"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Gamemodes(Base):
    __tablename__ = "gamemodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    zip = Column(Integer, index=True)
    city = Column(String, index=True)
