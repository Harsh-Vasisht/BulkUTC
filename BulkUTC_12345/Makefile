# Directories
SRC_DIR := src
TEST_DIR := tests
BUILD_DIR := build

# Commands
PHP := php
COMPOSER := composer
DOCKER := docker

# Files
DOCKERFILE := Dockerfile

# Phony targets
.PHONY: all build test clean docker-build docker-run install test-unit test-e2e start

# Default target
all: build

# Build the project
build:
	@echo "Building the project..."
	$(COMPOSER) install
	# Add any other build steps here

# Run all tests
test: build
	@echo "Running all tests..."
	$(MAKE) test-unit
	$(MAKE) test-e2e

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf $(BUILD_DIR)
	# Add any other cleanup steps here

# Build Docker image
docker-build:
	@echo "Building Docker image..."
	$(DOCKER) build -t bulkutc -f $(DOCKERFILE) .

# Run Docker container
docker-run:
	@echo "Running Docker container..."
	$(DOCKER) run -p 8080:80 bulkutc

# Install dependencies
install:
	@echo "Installing dependencies..."
	$(COMPOSER) install

# Run unit tests
test-unit: build
	@echo "Running unit tests..."
	$(PHP) $(TEST_DIR)/unit/library/test_library.py
	$(PHP) $(TEST_DIR)/unit/shopping_cart/test_cart.py
	$(PHP) $(TEST_DIR)/unit/university/test_university.py

# Run e2e tests
test-e2e: build
	@echo "Running e2e tests..."
	$(PHP) $(TEST_DIR)/e2e/test_e2e.py

# Start the application locally
start:
	@echo "Starting the application..."
	$(PHP) -S localhost:8080 -t $(SRC_DIR)