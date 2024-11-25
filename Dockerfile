# Use a stable and lightweight Python base image
FROM python:3.11-slim-bullseye

# Set the working directory for the application
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install system dependencies and clean up unnecessary files
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel to the latest stable versions
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install application dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Ensure the container runs as a non-root user for security (optional)
RUN useradd -ms /bin/bash appuser && chown -R appuser /app
USER appuser

# Set the default command to run the application
CMD ["python", "app.py"]