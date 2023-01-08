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
  - hashed_gamemode_key --> Hashed

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


# Postman

POST:

![post_gamemode_Postman](https://user-images.githubusercontent.com/81410142/211197941-0fc04c23-8090-497e-a7ae-8bfd4889bb20.png)
![post_class_postman](https://user-images.githubusercontent.com/81410142/211197928-d8f324d7-384d-4322-847e-74feae08c51a.png)
![post_location_postman](https://user-images.githubusercontent.com/81410142/211197946-5e37a5d3-3481-4750-bd2f-d6749e2cbb7d.png)

GET:

![get_gamemodes](https://user-images.githubusercontent.com/81410142/211197887-042dfd89-b802-4402-bcb4-aa80004bc498.png)
![get_classes](https://user-images.githubusercontent.com/81410142/211197893-aa71551c-64db-4119-ab10-2e1d09ebf419.png)
![get_locations](https://user-images.githubusercontent.com/81410142/211197898-69d7fdc8-20a3-40ed-92bc-10a823ca2ef8.png)

PUT:

![put_class_postman](https://user-images.githubusercontent.com/81410142/211197980-d26a45ed-9758-4dad-907a-2470c5c466ea.png)

DELETE:

![delete_classes](https://user-images.githubusercontent.com/81410142/211197991-e2dab434-2648-41df-8032-ae89840dddf7.png)


# Docker

![docker_compose](https://user-images.githubusercontent.com/81410142/211198162-6233fd42-6ef2-4543-af66-e033936f5420.png)
![workflow](https://user-images.githubusercontent.com/81410142/211198169-486adc7c-fa90-45d0-95a2-622aa57cb8a1.png)


# Okteto

![okteto](https://user-images.githubusercontent.com/81410142/211198033-c87c932c-0d32-459c-a1ef-3dc001a4e96d.png)

# Netlify
https://api-project2-jesse.netlify.app/
![front](https://user-images.githubusercontent.com/81410142/211198062-24edfa41-dd40-4cc5-8fae-e789fcad6919.png)












