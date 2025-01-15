# Use the official Python 3.9 slim image as the base
FROM python:3.9-slim

# Set environment variables to optimize behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the working directory
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "main.py"]
