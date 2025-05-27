.PHONY: init up

init:
	docker compose up airflow-init

up:
	docker compose up -d

down:
	docker compose down