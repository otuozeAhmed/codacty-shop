# Base build
FROM python:3.10-alpine as base
RUN apk add --update --upgrade --virtual .build-deps \
    build-base postgresql-dev \
    python3-dev libpq \
    fontconfig ttf-freefont \
    font-noto terminus-font \
    && fc-cache -f \
    && fc-list | sort 

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# multistage build
FROM python:3.10-alpine
RUN apk add libpq gtk+3.0 gettext
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY . /app
ENV PYTHONUNBUFFERED 1

WORKDIR /app

CMD [ "gunicorn", "--reload", "--timeout=300", "--workers=2", \
    "--worker-tmp-dir", "/dev/shm", "--bind=0.0.0.0:8000", "--chdir", \
    "/app", "core.wsgi:application" ]
