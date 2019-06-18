# filename references
DEV_FOLDER := docker
DEV_COMPOSE_FILE := docker/docker-compose.yml

build:
	@ echo "Building favorite_things..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} build
	@ echo "Finished building"
	@ echo "Starting services"
	@ docker-compose -f ${DEV_COMPOSE_FILE} up -d
	@ echo "Services started"

start:
	@ echo "Starting favorite_things..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} up -d
	@ echo "services started"

stop:
	@ docker stop "$(service)"

migrations:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DEV_FOLDER}/makemigrations.sh "$(message)"

migrate:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DEV_FOLDER}/migration.sh "$(message)"

migrate-down:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app alembic downgrade base

flask_shell:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app sh

mysql_shell:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec database bash
