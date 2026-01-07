# Base image with fixed Python version (production lock)
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (enables Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model
COPY src ./src

# Expose API port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
