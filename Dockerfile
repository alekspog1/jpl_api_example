FROM python:3.7-alpine
RUN mkdir -p /app
WORKDIR /app
COPY tests/requirements.txt  /app/
RUN apk add --no-cache --virtual .build-deps build-base python-dev     && apk add --no-cache jpeg-dev zlib-dev     && pip install --no-cache-dir -r requirements.txt     && apk del .build-deps
COPY tests/ /app/tests/
CMD ["pytest"]
