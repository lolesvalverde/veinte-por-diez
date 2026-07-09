FROM nginx:alpine

# Copy static assets and templates to Nginx web root
COPY static/ /usr/share/nginx/html/static/
COPY templates/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
