FROM python:3.10-slim

WORKDIR /app
COPY backend/ /app

RUN pip install flask pyjwt

EXPOSE 5000
CMD ["python", "app.py"]
