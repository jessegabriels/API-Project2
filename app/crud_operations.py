import random

from sqlalchemy.orm import Session
from random import randrange

import models
import schemas
import auth


def get_wclass(db: Session, wclass_id: int):
    return db.query(models.Wclass).filter(models.Wclass.class_id == wclass_id).first()


def get_gamemode(db: Session, gamemode_id: int):
    return db.query(models.Gamemodes).filter(models.Gamemodes.gamemode_id == gamemode_id).first()


def get_random_gamemode(db: Session):
    rows = db.query(models.Gamemodes).count()
    random_int = random.randrange(1, rows-1)
    return db.query(models.Gamemodes).filter(models.Gamemodes.gamemode_id == random_int).first()


def get_location(db: Session, location_id: int):
    returnq = db.query(models.Location).filter(models.Location.location_id == location_id).first()
    print(returnq)
    return returnq


def get_random_location(db: Session):
    rows = db.query(models.Location).count()
    random_int = random.randrange(1, rows - 1)
    return db.query(models.Location).filter(models.Location.location_id == random_int).first()


def get_gamemodes(db: Session, skip: int = 0, limit: int = 100):
    gamemodeList = []
    all_gamemodes = db.query(models.Gamemodes).offset(skip).limit(limit).all()
    for game in all_gamemodes:
        gamemodeList.append(game)

    print(gamemodeList)
    return gamemodeList


def get_wclasses(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Wclass).offset(skip).limit(limit).all()


def get_random_class(db: Session):
    rows = db.query(models.Wclass).count()
    random_int = random.randrange(1, rows - 1)
    return db.query(models.Wclass).filter(models.Wclass.class_id == random_int).first()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()


def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(location_name=location.location_name, zip=location.zip, city=location.city)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def create_wclass(db: Session, wclass: schemas.WclassCreate):
    db_wclass = models.Wclass(class_name=wclass.class_name)
    db.add(db_wclass)
    db.commit()
    db.refresh(db_wclass)
    return db_wclass


def create_gamemode(db: Session, gamemode: schemas.GamemodeCreate):
    hashed_gamemode_key = auth.get_gamemode_key_hash(gamemode.gamemode_key)
    db_gamemode = models.Gamemodes(gamemode_name=gamemode.gamemode_name, hashed_gamemode_key=hashed_gamemode_key)
    db.add(db_gamemode)
    db.commit()
    db.refresh(db_gamemode)
    return db_gamemode


def update_gamemode(db: Session, gamemode: schemas.Gamemodes):
    db_gamemode = models.Gamemodes(gamemode_name=gamemode.gamemode_name)
    db.add(db_gamemode)
    db.commit()
    db.refresh(db_gamemode)
    return db_gamemode


def update_class(db: Session, wclass: schemas.Wclass):
    db_class = models.Wclass(class_name=wclass.class_name)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class
