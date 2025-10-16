FROM debian:12

RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-php8.2 \
    php8.2-ctype \
    php8.2-curl \
    php8.2-dom \
    php8.2-fpm \
    php8.2-gd \
    php8.2-mbstring \
    php8.2-zip \
    php8.2-mysqli

COPY apache2-foreground /usr/local/bin/

RUN a2enmod rewrite

CMD ["apache2-foreground"]
