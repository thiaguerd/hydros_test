FROM python:3.9.0

RUN apt-get update

WORKDIR /app

RUN python3 -m venv venv

RUN . ./venv/bin/activate

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
