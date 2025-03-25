# Use a Python base image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy all application files to the container
COPY api/ /app/

# Install dependencies

RUN pip install --no-cache-dir -r api-requirements.txt


# Expose Flask app's port
EXPOSE 5000

# Run the Flask app
CMD ["python", "book_api.py"]