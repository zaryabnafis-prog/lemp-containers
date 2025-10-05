FROM nginx:1.27-alpine

# build context is ./frontend
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
