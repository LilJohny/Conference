FROM python:3.7
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt;python manage.py makemigrations;python manage.py migrate;
EXPOSE 8000
CMD exec gunicorn Conferences.wsgi:application --bind 0.0.0.0:8000 --workers 3