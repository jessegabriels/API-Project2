from sqlalchemy.orm import Session

import models
import schemas


def get_wclass(db: Session, wclass_id: int):
    return db.query(models.Wclass).filter(models.Wclass.id == wclass_id).first()


def get_gamemode(db: Session, gamemode_id: int):
    return db.query(models.Gamemodes).filter(models.Gamemodes.id == gamemode_id).first()


def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def get_locaiton_by_zip(db: Session, zip: int):
    return db.query(models.Location).filter(models.Location.zip == zip).first()


def get_gamemodes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Gamemodes).offset(skip).limit(limit).all()


def get_wclasses(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Wclass).offset(skip).limit(limit).all()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()


def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(name=location.name, zip=location.zip, city=location.city)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def create_wclass(db: Session, wclass: schemas.WclassCreate):
    db_wclass = models.Location(name=wclass.name)
    db.add(db_wclass)
    db.commit()
    db.refresh(db_wclass)
    return db_wclass


def create_gamemode(db: Session, gamemode: schemas.GamemodeCreate):
    db_gamemode = models.Location(name=gamemode.name)
    db.add(db_gamemode)
    db.commit()
    db.refresh(db_gamemode)
    return db_gamemode
