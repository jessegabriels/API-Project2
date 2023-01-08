# API-Project2

# Concept

Ik heb een Airsoft API gemaakt. Achter deze API zit een databank waarin een aantal speelvelden, gamemodes en wapenclasses in staan.
Het doel van deze API is om een gebruiker geen keuzenstress te geven. Het is ook makkelijk voor een teambuilding te organiseren, feestjes,...

Met deze API krijgt de gebruiker een speelveld toegewezen samen met een gamemode en een wapenuitrusting.

# GET endpoints

1)  GET random gamemode
2)  GET random location
3)  GET random class
4)  GET all gamemodes
5)  GET all locations
6)  GET all classes

![all_gets](https://user-images.githubusercontent.com/81410142/211197249-d8b94355-2bfa-47de-a6c1-54aec1030cd5.png)

# POST endpoints

1) POST gamemode
2) POST location
3) POST class

![all_posts](https://user-images.githubusercontent.com/81410142/211197343-961f6186-80fb-4e95-9a0f-4c4f82c84d12.png)

# DELETE endpoints

1) DELETE gamemode
2) DELETE location
3) DELETE class

![all_delete](https://user-images.githubusercontent.com/81410142/211197403-14af02e0-e15e-4c82-a48a-2214820c3e7f.png)

# PUT endpoints

1) PUT class
2) PUT gamemode

![all_put](https://user-images.githubusercontent.com/81410142/211197455-7d83288a-66ca-4a02-8047-e5cc0ecc109d.png)

# SQLite Database
Gamemodes:
  - gamemode_id
  - gamemode_name
  - hashed_gamemode_key

![sql_gamemode](https://user-images.githubusercontent.com/81410142/211197634-eb22e6e7-ad5a-4c60-9881-b88f9feaeb7d.png)

Class:
  - class_id
  - class_name

![sql_class](https://user-images.githubusercontent.com/81410142/211197665-e87bc0ea-4b5c-4b7f-8e57-d9eb8d307ba1.png)

Location:
  - location_id
  - location_name
  - zip
  - city

![sql_location](https://user-images.githubusercontent.com/81410142/211197712-30b46f0f-e0ba-444d-b7fc-467e533543df.png)























