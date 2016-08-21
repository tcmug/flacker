FROM alpine:3.4

RUN apk add --no-cache sudo git python uwsgi py-pip uwsgi-router_uwsgi uwsgi-python openssh && \
    rm -rf /var/cache/apk/*

RUN pip install paste flask flask-assets jsmin flask_wtf sqlalchemy flask_sqlalchemy flask_login

RUN mkdir -p /app/www && \
    adduser -D -s /bin/sh -h /app www

COPY run.sh /app
COPY uwsgi.ini /app/uwsgi.ini

RUN chown -R www:www /app

VOLUME ["/app/www"]

ENTRYPOINT ["/app/run.sh"]
