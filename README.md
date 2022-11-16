### Pre-requisites :
  - python >= 3.8.*
    - virutalenv or virtualenvwrapper
  - docker == 20.10.18
    - docker compose (plugin)

### OVapi :
  - wiki : https://github.com/koch-t/KV78Turbo-OVAPI/wiki

### Execute step by step on your linux machine:

#### Docker Compose
- ```docker compose -f docker-compose.yml up -d```
- ```docker ps``` (make sure containers are up)

#### Poetry
- TODO

### PGadmin:
  - http://0.0.0.0:8080/
    - username: user@domain.com
    - password: SuperSecret
  - once connected to pgadmin; connect to the local database instance
    - username: postgres
    - password: postgres
    - database: postgres
- check table ```public.ods_line``` on ```postgres``` database