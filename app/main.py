from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud_operations
import models
import schemas
from databse import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

project = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#@app.post("/users/", response_model=schemas.User)
#def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#    db_user = crud.get_user_by_email(db, email=user.email)
#    if db_user:
#        raise HTTPException(status_code=400, detail="Email already registered")
#    return crud.create_user(db=db, user=user)


@project.get("/gamemodes/", response_model=list[schemas.Gamemodes])
def read_gamemodes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gamemodes = crud_operations.get_gamemodes(db, skip=skip, limit=limit)
    return gamemodes


@project.get("/gamemodes/{gamemode_id}", response_model=schemas.Gamemodes)
def read_gamemode(gamemode_id: int, db: Session = Depends(get_db)):
    db_gamemode = crud_operations.get_gamemode(db, gamemode_id=gamemode_id)
    if db_gamemode is None:
        raise HTTPException(status_code=404, detail="Gamemode not found")
    return db_gamemode


@project.get("/classes/", response_model=list[schemas.Wclass])
def read_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes = crud_operations.get_wclasses(db, skip=skip, limit=limit)
    return classes


@project.get("/locations/", response_model=list[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud_operations.get_locations(db, skip=skip, limit=limit)
    return locations


#@app.post("/users/{user_id}/items/", response_model=schemas.Item)
#def create_item_for_user(
#    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
#):
#    return crud.create_user_item(db=db, item=item, user_id=user_id)


#@app.get("/items/", response_model=list[schemas.Item])
#def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    items = crud.get_items(db, skip=skip, limit=limit)
#    return items