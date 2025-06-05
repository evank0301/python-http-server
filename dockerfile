FROM python:3

WORKDIR /usr/src/httpserver

COPY . .
CMD ["python", "./app.py"]
