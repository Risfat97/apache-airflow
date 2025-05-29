.PHONY: init up down bash

init:
	docker compose up airflow-init

up:
	docker compose up -d

down:
	docker compose down

clean:
	docker compose down --volumes --remove-orphans

bash:
	docker compose exec -it airflow-scheduler bash