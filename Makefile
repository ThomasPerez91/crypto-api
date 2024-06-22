# Makefile

# Define a variable for the message with a default value
MESSAGE ?= "Create_a_baseline_migrations"

# Rule to run alembic command in the /project directory
migration:
	@cd project && alembic revision --autogenerate -m "$(MESSAGE)"

# Rule to start the containers
start:
	@docker-compose up -d

# Rule to stop the containers
stop:
	@docker-compose down

# Rule to remove containers, networks, volumes, and images created by `up`
remove:
	@docker-compose down --volumes --rmi all

# Rule to recreate the containers
recreate: remove start
