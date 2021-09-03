FROM python:alpine3.14

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

ENV FLASK_HOST="0.0.0.0"
ENV FLASK_PORT=5000
ENV FLASK_DEBUG=False

CMD ["python", "main.py"]
