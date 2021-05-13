FROM python:3.9-slim

COPY ./src /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip intall -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src/main:app", "--host=0.0.0.0", "--reload"]