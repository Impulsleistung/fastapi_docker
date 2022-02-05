# 1. FastAPI Docker

In this project, the implementation of FastAPI is demonstrated and executed in a Docker container. The repository is managed on GitHub and executed in a container instance on a UBUNTU/DOCKER.

Techstack:

- FastAPI / pydantic
- UVICORN
- GitHub
- Docker -> Python:3.9
- Digitalocean

Toolstack:

- Visual Studio Code
- SSH
- Thunder Client (REST API Testing)

The submitted code and the configurations are entirely executable. In the future, it is conceivable that further containers will be added and a storage volume will be stored. The FastAPI server is started for test purposes on the local UBUNTU environment as follows:

`uvicorn main:app --reload`

## 1.1. References

Here is everything you need to understand the repository

### 1.1.1. Docker

- [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)

### 1.1.2. Fast API

- [FastAPI Tutorial - Building RESTful APIs with Python](https://www.youtube.com/watch?v=GN6ICac3OXY)

### 1.1.3. Rest Testing

- [Thunder Client](https://www.thunderclient.com/)

## 1.2. Build process

### 1.2.1. Reset the Docker completely (make it naked)

`docker kill $(docker ps -q)`

`docker rm $(docker ps -a -q)`

`docker rmi $(docker images -q)`

### 1.2.2. Build the container from the ground up

`kevin@impulsleistung:~/$ docker build -t myimage .`

### 1.2.3. Run it

`kevin@impulsleistung:~/$ docker run -d --name mycontainer2 -p 8080:8080 myimage`

## 1.3. Check the running status

`kevin@impulsleistung:~/fastapi_pandas$ docker ps`

## 1.4. Fetch the IP-Adress to see the FastAPI

`kevin@impulsleistung:~/$ hostname -I`

## 1.5. Access the FastAPI

> <http://164.90.236.185:8080/api/v1/users>

## 1.6. The interactive testing can be done here

> <http://164.90.236.185:8080/docs>
