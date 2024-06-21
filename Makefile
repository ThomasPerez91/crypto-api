NAME ?= "Create a baseline migrations"

migration:
    @cd project && alembic revision --autogenerate -m "$(NAME)"

# Start the containers
start:
    docker-compose up -d

# Stop the containers
stop:
    docker-compose down

# Remove containers, networks, volumes, and images created by `up`
remove:
    docker-compose down --volumes --rmi all

# Recreate the containers
recreate: remove start