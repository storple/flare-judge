FROM nginx

#ARG DOMAIN_NAME

RUN rm /etc/nginx/conf.d/default.conf

COPY ./app_server.conf /etc/nginx/templates/app_server.conf.template
COPY ./nginx.conf /etc/nginx/nginx.conf

ENV CL_FILE=/etc/nginx/conf.d/cloudflare_ips.conf 

RUN touch $CL_FILE
RUN \
for x in $(curl https://www.cloudflare.com/ips-v4); do echo "set_real_ip_from $x;" >> $CL_FILE; done && \
for x in $(curl https://www.cloudflare.com/ips-v6); do echo "set_real_ip_from $x;" >> $CL_FILE; done && \
 echo "real_ip_header CF-Connecting-IP;" >> $CL_FILE
#COPY ./env/${DOMAIN_NAME}.pem /etc/ssl/
#COPY ./env/${DOMAIN_NAME}.key /etc/ssl/
