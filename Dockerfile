FROM python:3.7-alpine3.12
RUN mkdir -p /app
WORKDIR /app
COPY tests/requirements.txt  /app/
RUN apk add --no-cache --virtual .build-deps build-base python3-dev     && apk add --no-cache jpeg-dev zlib-dev     && pip install --no-cache-dir -r requirements.txt     && apk del .build-deps
COPY tests/ /app/tests/
CMD ["pytest"]
