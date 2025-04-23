FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN python3 -m venv venv
RUN ./venv/bin/pip install -r requirements.txt
COPY backend/ /app/
EXPOSE 5000
CMD ["./venv/bin/python", "app.py"]
