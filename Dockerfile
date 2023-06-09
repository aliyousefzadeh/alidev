FROM nginx
RUN apt-get update
RUN apt-get install vim
COPY . /usr/share/nginx/html
COPY --from=build alidev.conf /etc/nginx/conf.d/alidev.conf
