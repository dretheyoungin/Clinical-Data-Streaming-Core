# 1. Use the official lightweight Python runtime environment from Docker Hub
FROM python:3.10-slim

# 2. Set a secure, isolated working directory inside the virtual cloud server
WORKDIR /app

# 3. Copy our Python script from your laptop straight into the cloud container
COPY principal_streaming_core.py .

# 4. Set the environment variable to ensure logs stream instantly to the console
ENV PYTHONUNBUFFERED=1

# 5. Define the execution hook command to run the streaming data engine automatically
CMD ["python", "principal_streaming_core.py"]