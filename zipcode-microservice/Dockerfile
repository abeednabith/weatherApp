# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install the required packages
RUN pip install Flask
RUN pip install requests
RUN pip install json

# Copy the application code to the container
COPY zipcode.py .

# Set the environment variable for Flask
ENV FLASK_APP=zipcode.py

# Expose port 5001 for the Flask app to listen on
EXPOSE 5001

# Specify the command to run when the container starts
CMD ["python", "zipcode.py"]