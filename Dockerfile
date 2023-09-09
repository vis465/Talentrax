FROM python:3.10

ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install --upgrade pip
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 8000

CMD ["python","manage.py","runserver"]