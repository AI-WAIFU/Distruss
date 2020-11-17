FROM python:3.8-alpine
WORKDIR /code
ENV FLASK_APP=src
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual \
  .build-deps \
  gcc \
  make \
  musl-dev \
  postgresql-dev \
  libev-dev \
  libressl-dev \
  musl-dev \
  libffi-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
