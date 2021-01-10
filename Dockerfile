# set base image
FROM python:3.8-slim

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to temp directory
COPY app/requirements.txt /tmp/

# install dependencies
RUN pip install -r /tmp/requirements.txt

# copy the content of the local src directory to the working directory
COPY app /app

# run container as executable on start
ENTRYPOINT python -u main.py
