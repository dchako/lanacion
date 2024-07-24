FROM python:3.10

ENV PYTHONPATH=/app

RUN groupadd --gid 1000 user && useradd --uid 1000 --gid 1000 -m user

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

ARG requirements=/app/requirements.txt
RUN pip install -r ${requirements}


ENTRYPOINT ["./docker/api/entrypoint.sh"]