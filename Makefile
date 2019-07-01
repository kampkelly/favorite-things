# filename references
DOCKER_FOLDER := docker
DEV_COMPOSE_FILE := docker/dev/docker-compose.yml
RELEASE_COMPOSE_FILE := docker/release/docker-compose.yml

build:
	@ echo "Building favorite_things..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} build
	@ echo "Finished building"
	@ echo "Starting services"
	@ docker-compose -f ${DEV_COMPOSE_FILE} up
	@ echo "Services started"

start:
	@ echo "Starting favorite_things..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} up
	@ echo "services started"

release:
	@ echo "Building release favorite_things..."
	@ docker-compose -f ${RELEASE_COMPOSE_FILE} build
	@ echo "Finished building"
	@ echo "Starting services"
	@ docker-compose -f ${RELEASE_COMPOSE_FILE} up
	@ echo "Services started"

start-release:
	@ echo "Starting release favorite_things..."
	@ docker-compose -f ${RELEASE_COMPOSE_FILE} up
	@ echo "services started"

stop:
	@ docker stop "$(service)"

migrations:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec api ../${DOCKER_FOLDER}/makemigrations.sh "$(message)"

migrate:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec api ../${DOCKER_FOLDER}/migration.sh "$(message)"

migrate-down:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec api alembic downgrade base

flask_shell:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec api sh

client_shell:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec client sh

mysql_shell:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec database bash

nginx_shell:
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec nginx bash

test:
	@ echo 'starting tests...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DOCKER_FOLDER}/start_tests.sh "$(test)"

logs:
	@ echo 'Getting logs...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} logs

logs_prod:
	@ echo 'Getting logs...'
	@ docker-compose -f ${RELEASE_COMPOSE_FILE} logs
