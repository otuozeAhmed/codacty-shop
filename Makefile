ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs

migrate:
	docker compose exec shop_app python3 /app/manage.py migrate

shell:
	docker compose exec shop_app sh

makemigrations:
	sudo docker compose exec shop_app python3 /app/manage.py makemigrations

superuser:
	docker compose exec shop_app python3 /app/manage.py createsuperuser 

collectstatic:
	docker compose exec shop_app python3 /app/manage.py collectstatic --no-input --clear

down-v:
	docker compose down -v

volume:
	docker volume inspect db

db:
	docker compose exec postgres-db psql --username=postgres --dbname=postgres

test:
	docker compose exec shop_app pytest -p no:warnings --cov=.

test-html:
	docker compose exec shop_app pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker compose exec shop_app flake8 .

black-check:
	docker compose exec shop_app black --check --exclude=migrations .

black-diff:
	docker compose exec shop_app black --diff --exclude=migrations .

black:
	docker compose exec shop_app black --exclude=migrations .

isort-check:
	docker compose exec shop_app isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose exec shop_app isort . --diff --skip env --skip migrations

isort:
	docker compose exec shop_app isort . --skip env --skip migrations