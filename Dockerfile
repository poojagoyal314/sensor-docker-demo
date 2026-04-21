FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt   .
RUN pip install --no-cache-dir -r requirements.txt
COPY sensor_pipeline.py  .
CMD ["python", "sensor_pipeline.py"]
