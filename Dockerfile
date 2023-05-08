# FROM mysql:8

# RUN pip install mysql-connector-python
# WORKDIR /user/app/src
# ENV MYSQL_ROOT_PASSWORD pass
# COPY ./hexflow.sql /docker-entrypoint-initdb.d/hexflow.sql


# FROM mysql/mysql-server:8.0

# COPY ./docker/db/init_db.sh /docker-entrypoint-initdb.d/
# RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh





# base image  
FROM python:3.11.0-slim-buster
# setup environment variable  
# ENV DockerHOME=/home/app/webapp  

# set work directory  
# RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR /django

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
# COPY . $DockerHOME  
COPY . .

COPY requirements.txt requirements.txt
# run this command to install all dependencies  
RUN pip install -r requirements.txt 


# port where the Django app runs  
# EXPOSE 8000  
# start server  
CMD python manage.py runserver 0.0.0.0:8000
# CMD ["python" , "manage.py", "runserver" , "0.0.0.0:8000"]
