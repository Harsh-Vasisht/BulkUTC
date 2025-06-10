# Build stage
FROM composer:2 as build

WORKDIR /app
COPY . /app
RUN composer install --no-dev --no-scripts --no-autoloader

# Production stage
FROM php:8.1-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

# Set working directory
WORKDIR /var/www

# Copy application files
COPY --chown=www-data:www-data . /var/www
COPY --from=build --chown=www-data:www-data /app/vendor /var/www/vendor

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Generate optimized autoload files
RUN composer dump-autoload --optimize

# Use the default production configuration
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

# Expose port 9000 for PHP-FPM
EXPOSE 9000

# Set www-data as the owner of the working directory
RUN chown -R www-data:www-data /var/www

# Switch to non-root user
USER www-data

# Start PHP-FPM
CMD ["php-fpm"]