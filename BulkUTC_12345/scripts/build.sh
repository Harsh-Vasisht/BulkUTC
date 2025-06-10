#!/bin/bash

# build.sh - Build script for BulkUTC_12345 project

# Set strict mode
set -euo pipefail

# Environment variables
ENV=${1:-development}
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="${PROJECT_ROOT}/build"
DOCKER_IMAGE_NAME="bulkutc-12345"
DOCKER_IMAGE_TAG="latest"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

check_command() {
    if ! command -v "$1" &> /dev/null; then
        log_error "$1 could not be found. Please install it and try again."
        exit 1
    fi
}

# Check required commands
check_command php
check_command composer
check_command docker

# Main build function
main() {
    log_info "Starting build process for environment: $ENV"

    # Create build directory
    mkdir -p "$BUILD_DIR"

    # Install PHP dependencies
    log_info "Installing PHP dependencies..."
    composer install --no-dev --optimize-autoloader

    # Run PHP linter
    log_info "Running PHP linter..."
    find "$PROJECT_ROOT/src" -name "*.php" -print0 | xargs -0 -n1 php -l

    # Run unit tests
    log_info "Running unit tests..."
    php vendor/bin/phpunit tests/unit

    # Run e2e tests
    log_info "Running e2e tests..."
    php vendor/bin/phpunit tests/e2e

    # Build Docker image
    if [ "$ENV" = "production" ]; then
        log_info "Building Docker image..."
        docker build -t "${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}" .
    else
        log_warn "Skipping Docker image build for non-production environment"
    fi

    # Run Makefile targets if available
    if [ -f "$PROJECT_ROOT/Makefile" ]; then
        log_info "Running Makefile targets..."
        make -C "$PROJECT_ROOT" build
    fi

    # Copy necessary files to build directory
    log_info "Copying files to build directory..."
    cp -R "$PROJECT_ROOT/src" "$BUILD_DIR/"
    cp -R "$PROJECT_ROOT/config" "$BUILD_DIR/"
    cp "$PROJECT_ROOT/Dockerfile" "$BUILD_DIR/"
    cp "$PROJECT_ROOT/requirements.txt" "$BUILD_DIR/"

    log_info "Build process completed successfully!"
}

# Error handling
handle_error() {
    log_error "An error occurred on line $1. Exiting..."
    exit 1
}

trap 'handle_error $LINENO' ERR

# Run the main function
main

exit 0