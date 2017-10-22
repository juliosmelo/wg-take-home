FROM python:3.6.2-onbuild
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD gunicorn chocfruitbox.wsgi