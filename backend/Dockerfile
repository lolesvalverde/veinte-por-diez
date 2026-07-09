FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if any
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend and frontend source files to preserve the relative paths
COPY backend/ ./backend/
COPY frontend/ ./frontend/

EXPOSE 8500

WORKDIR /app/backend
CMD ["python", "app.py"]
