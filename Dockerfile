# start with Python base image
FROM python:3.12.2-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY src/ src/
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    -r requirements.txt

# expose port
EXPOSE 8001

# run FastAPI application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
