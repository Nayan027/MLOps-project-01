# Use an official Python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy your application code
COPY . /app

# Install the dependencies
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt  
# Ensure gunicorn is installed

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app
# CMD ["python3", "app.py"]
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "app:app"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]