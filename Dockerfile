FROM python:3.12-slim

# Set environment variables to ensure Python behaves correctly in containers
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container to /app
WORKDIR /app

# Install dependencies needed for MySQL client and netcat
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    libssl-dev \
    libffi-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*


# Copy the entire project (including manage.py) into the container's /app directory
COPY . /app/

# Install Python dependencies from the requirements.txt file
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Set the entrypoint to run Django's development server
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
