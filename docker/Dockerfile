FROM python:3.8.2-buster
ENV PYTHONUNBUFFERED 1

RUN \
  echo "deb https://deb.nodesource.com/node_12.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs yarn && \
  pip install -U pip && pip install pipenv && \
  npm i -g npm@^6 && \
  rm -rf /var/lib/apt/lists/*

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

RUN cd frontend && npm install && npm run dev


RUN /app/manage.py collectstatic --no-input
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8005", "-w", "2",  "-k", "uvicorn.workers.UvicornWorker", "tinyurl.asgi:application"]

EXPOSE 8433
