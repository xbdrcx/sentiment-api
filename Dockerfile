FROM python:3.10-slim
WORKDIR /app/app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY app/ .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]