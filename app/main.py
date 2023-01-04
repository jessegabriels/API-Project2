from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud_operations
import models
import schemas
from databse import SessionLocal, engine
import os

from fastapi.middleware.cors import CORSMiddleware

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

project = FastAPI()

# link naar okteto: https://airsoft-api-service-jessegabriels.cloud.okteto.net

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "https://jessegabriels.github.io",
    "https://jessegabriels.github.io/API-Project2-Front/*",
    "https://jessegabriels.github.io/API-Project2-Front/index.html"
]

project.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#    db_user = crud.get_user_by_email(db, email=user.email)
#    if db_user:
#        raise HTTPException(status_code=400, detail="Email already registered")
#    return crud.create_user(db=db, user=user)

@project.get("/gamemodes/", response_model=list[schemas.Gamemodes])
def read_gamemodes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gamemodes = crud_operations.get_gamemodes(db, skip=skip, limit=limit)
    return gamemodes



#@project.get("/gamemodes/{gamemode_id}", response_model=schemas.Gamemodes)
#def read_gamemode(gamemode_id: int, db: Session = Depends(get_db)):
#    db_gamemode = crud_operations.get_gamemode(db, gamemode_id=gamemode_id)
    #if db_gamemode is None:
    #    raise HTTPException(status_code=404, detail="Gamemode not found")
    #return db_gamemode


@project.get("/gamemodes/{gamemode_id}", response_model=schemas.Gamemodes)
def read_gamemode(gamemode_id: int, db: Session = Depends(get_db)):
    db_gamemode = crud_operations.get_gamemode(db, gamemode_id=gamemode_id)
    #if db_gamemode is None:
       # raise HTTPException(status_code=404, detail="Gamemode not found")
    return {"name": db_gamemode.gamemode_name, "id": db_gamemode.gamemode_id}



@project.get("/classes/", response_model=list[schemas.Wclass])
def read_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes = crud_operations.get_wclasses(db, skip=skip, limit=limit)
    return classes


@project.get("/locations/", response_model=list[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud_operations.get_locations(db, skip=skip, limit=limit)
    return locations


@project.post("/gamemodes/", response_model=schemas.Gamemodes)
def create_gamemode(gamemode_name: schemas.GamemodeCreate, db: Session = Depends(get_db)):
    new_gamemode = crud_operations.create_gamemode(db=db, gamemode=gamemode_name)
    return new_gamemode


@project.post("/classes/", response_model=schemas.Wclass)
def create_class(class_name: schemas.WclassCreate, db: Session = Depends(get_db)):
    new_class = crud_operations.create_wclass(db=db, wclass=class_name)
    return new_class


@project.post("/locations/", response_model=schemas.Location)
def create_location(location_name: schemas.LocationCreate, db: Session = Depends(get_db)):
    new_location = crud_operations.create_location(db=db, location=location_name)
    return new_location


@project.delete("/gamemodes/{gamemode_id}/")
def delete_gamemode(gamemode_id: int):
    with Session(engine) as session:
        gamemode = session.get(models.Gamemodes, gamemode_id)
        if not gamemode:
            raise HTTPException(status_code=404, detail="Gamemode not found")
        session.delete(gamemode)
        session.commit()
        return {"Done": True}


#PUT endpoint to update an existing gamemode
@project.put('/gamemodes/{gamemode_id}', response_model=schemas.Gamemodes)
def update_gamemode(gamemode_id: int, gamemode_name: str):
    session = Session(bind=engine, expire_on_commit=False)
    gamemode = session.query(models.Gamemodes).get(gamemode_id)
    if gamemode:
        gamemode.gamemode_name = gamemode_name
        session.commit()
    session.close()
    if not gamemode:
        raise HTTPException(status_code=404, detail=f"driver with id {gamemode_id} not found")

    return gamemode













