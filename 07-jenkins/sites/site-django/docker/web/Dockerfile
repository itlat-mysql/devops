# pull official base image
FROM python:3.12-bookworm

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install entrypoint dependencies
RUN apt update
RUN apt install netcat-traditional -y

# copy project
COPY . /app

# install python dependencies
RUN pip install -r requirements.txt

# Make entrypoint executable
RUN chmod +x /app/docker/web/entrypoint.sh

# run entrypoint
ENTRYPOINT ["bash", "/app/docker/web/entrypoint.sh"]