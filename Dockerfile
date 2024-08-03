FROM node:bookworm-slim AS nodejs

FROM python:3.10-bookworm

EXPOSE 8000

ARG ENV_FILE
ENV ENV_FILE ${ENV_FILE}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setup an app user so the container doesn't run as the root user
RUN useradd appuser

RUN mkdir -p /home/appuser/app && chown -R appuser /home/appuser

WORKDIR /home/appuser/app

COPY --from=nodejs /usr/local/bin /usr/local/bin
COPY --from=nodejs /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/npm
RUN npm install -g npm && \
npm install -g katex

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

RUN mkdir -p ./templates/generated

COPY --chown=appuser . .

RUN --mount=type=secret,id=web_env_build,target=${ENV_FILE},uid=1000 \
python manage.py tailwind install --no-input && \
python manage.py tailwind build --no-input && \
python manage.py collectstatic --no-input --clear

CMD \
python manage.py migrate --no-input && \
gunicorn flare.wsgi:application --bind 0.0.0.0:8000 --workers 7
