FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install kafka-python redis fastapi uvicorn
CMD ["python", "producer.py"]