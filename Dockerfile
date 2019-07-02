# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=conference Version=0.0.1
EXPOSE 8000

WORKDIR /app
ADD . /app

# Using pip:
RUN apt-get update && apt-get install -y \
        python-dev python3-pip python3-setuptools \
        libffi-dev libxml2-dev libxslt1-dev \
          zlib1g-dev libfreetype6-dev \
        liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "-m", "manage.py","runserver"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "conference"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m conference"
