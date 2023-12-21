FROM python:3.11-alpine

COPY . /taskdir

COPY ./requirements.txt /taskdir/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /taskdir/requirements.txt

EXPOSE 6060
WORKDIR taskdir

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py runserver

CMD ["gunicorn", "--bind", "0.0.0.0:6060", "--workers", "1", "placebo25.wsgi:application"]