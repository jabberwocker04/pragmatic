FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/jabberwocker04/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=vz2d_btiatmbz9kptqp2rn!cnzrg31nzn+n_wa8r+n4srz#c7g" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]