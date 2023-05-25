FROM nginx
RUN apt-get update
RUN apt-get install vim
COPY . /usr/share/nginx/html
