FROM python:3.9
ENV PYTHONUNBUFFERED=1

# Copy Files
WORKDIR /app
COPY /src/ /app/

# Install Requirements
RUN pip install -r requirements.txt

# Run App
WORKDIR /app/streamer
CMD ["python3.9","app.py"]