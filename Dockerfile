FROM python:3.8.2

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

CMD ["sh", "entrypoint.sh"]