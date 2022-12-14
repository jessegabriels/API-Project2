FROM python:3.10.0-slim
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install argon2_cffi
COPY ./app /code
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "main:project", "--host", "0.0.0.0", "--port", "8000"]
