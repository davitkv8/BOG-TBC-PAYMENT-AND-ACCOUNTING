# TBC/BOG External APIS with FASTAPI & microservices

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

- create startup.py script which corresponds all beginning processes
- add alembic for migrations at the beginning
- dockerize all processes, check for volumes/networks work correctly
- simple test framework integration (CI/CD OR JUST SIMPLE MANUAL TEST)
- add layers or encryptors for additional security for our passwords
- change print statements to responsive logging 

