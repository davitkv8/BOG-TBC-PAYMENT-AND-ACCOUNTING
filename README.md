# TBC/BOG External APIS with FASTAPI & microservices

# Description

```
    This project allows user to easly configure prodoction paramerts for Bank of Georgia and TBC Bank payment and accounting services.
    If you're BOG contractor, for access BOG provides Oauth2 authentication system. (it is not automated yet)
    
    If you're TBC contractor, for access TBC provides : 
    1) DGpass physical device
    2) certificate files (cert, key, pfx files)
    3) username and password 
    
    you have to configure all of them in ./Docker/env_files/.env.certificates file
    
    The idea of project is that, it will automatically sync data (Balances, Money Movements) from your provider's API (BOG or TBC in this case).
    And also gives you ability to make 2 kinds of payment scenarions very easly -
    1) Transfer between your own accs
    2) Transfer between your own acc to anyone else
    
    
    
```

# how to deploy

```
    The project start process is autamoted and
     it should run on your local machine directly if you follow all the steps.
    
    If you are Windows user, clone this project using following command -
            git clone https://github.com/someuser/somerepo --config core.autocrlf=false
    Or try another ways to turn off autocrlf
```


0. clone this repository
1. install docker & docker compose
1. cd to folder where app.py is living
1. run

```bash
    docker compose build --parallel && docker compose up --build -d
```

5. Wait for services to start - it should take no more than 10-15 seconds as we explicitely wait 3-5 minutes for first run
6. if \* is successfull, website should be available on: http://localhost:8000

# If any errors occurred
    Just be sure that you have execute privilegies for *.sh files inside ./Docker folder.

# Final Step (For TBC APIs)

```
    If you have ran the project correctly, check http://localhost:8000/docs
    For your first run, TBC API's do not work directly. 
    here are some additional steps you should follow to verify your docker host for TBC external API server.
    
    1) Take your GDPASS device.
    2) Run - docker exec -it banking__app python gdpass.py
    
```

# todo
- BOG system
- create startup.py script which corresponds all beginning processes
- add alembic for migrations at the beginning
- dockerize all processes, check for volumes/networks work correctly
- simple test framework integration (CI/CD OR JUST SIMPLE MANUAL TEST)
- add layers or encryptors for additional security for our passwords
- change print statements to responsive logging 
- add GDPASS verification process as API 
- change print statements to logging system
