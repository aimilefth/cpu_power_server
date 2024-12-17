# Use the official Python 3.12 image as our base
FROM python:3.12-slim

# Create a working directory
WORKDIR /app

# Copy code into the container
COPY code/ /app/

# Install necessary packages
RUN pip install pyJoules requests flask

# Expose port 5000 (or whichever port you want to use)
EXPOSE 5000

# Run the Flask server
CMD ["python", "flask_server.py"]