# Use an official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the microservice code to the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=weather.py

# Expose port 5002 for the Flask app to listen on
EXPOSE 5002

# Set the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]