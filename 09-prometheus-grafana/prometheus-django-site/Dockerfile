# pull official base image
FROM python:3.12-bookworm

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /app

# install python dependencies
RUN pip install -r requirements.txt

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# run entrypoint
ENTRYPOINT ["bash", "/app/entrypoint.sh"]