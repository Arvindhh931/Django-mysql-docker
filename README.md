# Django-mysql-docker

CRUD operation using Django Framework with MySQL Database 

## Running a docker container 

```bash
docker run --name new-db -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12345 -e MYSQL_ROOT_HOST='%' mysql/mysql-server:8.0.0
```

`-e MYSQL_ROOT_HOST='%'`: This flag sets the environment variable `MYSQL_ROOT_HOST` within the container to "%," which means the root user can connect to the MySQL server from any host (wildcard).

> [!NOTE] very important info
> **MYSQL_ROOT_HOST**: This variable specifies which hosts are allowed to connect to the MySQL server as the root user. By default, it's set to "localhost," meaning only connections from the same container are allowed. Setting it to "%" allows connections from any host.

> [!NOTE] important note
> `-`: Anything after the image name is treated as the command to run inside the container. In this case, the command is empty ("-"), which means it uses the default command specified in the Docker image, typically starting the MySQL server.

## Running docker container with volume mounted

```bash
docker run --name new-db -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12345 -e MYSQL_ROOT_HOST='%' -v /home/ik100047/Documents/container_data/:/var/lib/mysql mysql/mysql-server:8.0.0
```

docker image will be downloaded from docker hub

Django project - first_project
Application_1 - login

![](https://github.com/Arvindhh931/Django-mysql-docker/blob/main/Images/Screenshot%20from%202023-09-26%2013-43-31.png)

## model.py of login

![](https://github.com/Arvindhh931/Django-mysql-docker/blob/main/Images/Screenshot%20from%202023-09-26%2013-42-34.png)

## Migrating configurations and details to database

```python
python manage.py migrate
```

![](https://github.com/Arvindhh931/Django-mysql-docker/blob/main/Images/Screenshot%20from%202023-09-26%2013-40-17.png)

## Migrating configurations and details to database

```python
python manage.py makemigrations <application_name>
```

**migrations** directory will be generated with files like **initial_001.py**, 

```python
python manage.py migrate <application_name>
```

tables gets created from the **model.py** of **login app**

![](https://github.com/Arvindhh931/Django-mysql-docker/blob/main/Images/Screenshot%20from%202023-09-26%2013-40-37.png)

### Example 

```python
python manage.py makemigrations login
```

```python
python manage.py migrate login
```

![](https://github.com/Arvindhh931/Django-mysql-docker/blob/main/Images/Screenshot%20from%202023-09-26%2013-38-39.png)

