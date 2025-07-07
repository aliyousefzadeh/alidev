# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY bot/ /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "horoscop.py"]


# FROM nginx
# RUN apt-get update
# RUN apt-get install vim
# COPY . /usr/share/nginx/html
# COPY --from=build alidev.conf /etc/nginx/conf.d/alidev.conf
