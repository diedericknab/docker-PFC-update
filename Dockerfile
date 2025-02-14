# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the required libraries
RUN pip install --no-cache-dir paramiko

# Make port 22 available to the world outside this container
EXPOSE 22

# Run main.py and keep the container alive for a specified amount of time
CMD ["sh", "-c", "python ./main.py 2>/dev/null"]