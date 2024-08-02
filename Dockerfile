# Use the official Python base image
FROM python:3

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . /code/
