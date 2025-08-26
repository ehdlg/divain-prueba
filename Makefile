# Variables
DC := docker compose
API_SERVICE := api
DB_SERVICE := db

# Default target
.DEFAULT_GOAL := help

.PHONY: help
help: ## Show all commands list
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start: ## Build Docker image without using the cache
	$(DC) build --no-cache

.PHONY: up
up: ## Start Docker containers
	$(DC) up -d

.PHONY: down
down: ## Stop Docker containers
	$(DC) down

.PHONY: setup_db
setup_db: ## Setup the database tables
	$(DC) up -d $(API_SERVICE) $(DB_SERVICE)
	$(DC) exec -T $(API_SERVICE) python -m app.db.setup

.PHONY: populate_db
populate_db: ## Populate the database with test data
	$(DC) up -d $(API_SERVICE) $(DB_SERVICE)
	$(DC) exec -T $(API_SERVICE) python -m app.db.populate_db

.PHONY: setup
setup: setup_db populate_db ## Setup the database and populate it

.PHONY: init
init: start up setup ## Build Docker images and initialize DB with test data
	@echo "✅ Project initialized."
