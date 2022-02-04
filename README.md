# Fast API and pandas

## Why

The technical solution of "Fast API" will be demonstrated. The API will runs with
> uvicorn main:app --reload
in the local environment



 in a cloud environment and in interaction with Python/Pandas data types. The use of a container-based architecture is preferred as the solution should be modular and scalable. The architecture is sketched for better understanding

Since we deploy and commit, the following understanding of Git is crucial:

![GitHub Workflow](doc/git_workflow.png)

Remarks: Deployment in AZURE as WebApp possible

## How we do it

## Docker

* [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)

## Fast API

* [FastAPI Tutorial - Building RESTful APIs with Python](https://www.youtube.com/watch?v=GN6ICac3OXY)

## Rest Testing

* [Thunder Client](https://www.thunderclient.com/)

# Build process
## Reset the Docker completely by

> docker kill $(docker ps -q)
> docker rm $(docker ps -a -q)
> docker rmi $(docker images -q)

## Build it all from the ground

> kevin@impulsleistung:~/fastapi_pandas$ docker build -t myimage .
Sending build context to Docker daemon  615.9kB

## Run it
> kevin@impulsleistung:~/fastapi_pandas$ docker run -d --name mycontainer2 -p 8080:8080 myimage

## Check the running status
kevin@impulsleistung:~/fastapi_pandas$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                       NAMES
3b63fb214919   myimage   "uvicorn app.main:ap…"   47 seconds ago   Up 47 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   mycontainer2

## Fetch the IP-Adress
kevin@impulsleistung:~/fastapi_pandas$ hostname -I
164.90.236.185 10.19.0.5 

## Access the api
http://164.90.236.185:8080/api/v1/users

