# Apache Airflow v3.x

This is the documentation for installing Apache Airflow v3.x on Docker with a PostgreSQL database.


## Requirements
- Docker
- Docker Compose


## Required steps

1. `mkdir -p ./dags ./logs ./plugins`
2. `cp .env.example .env`, then edit the `.env` file to set your custom values.
3. If you are on linux or macOS you can use the following command to run Apache Airflow:
   ```bash
    make init    # Initialize the database
   ```
   
   ```bash
    make up      # Start the Airflow services
   ```
   
   Or you can run the following commands:
   ```bash
    docker compose exec airflow-webserver airflow db init
   ```
   
   ```bash
    docker compose up -d
   ```
   
## Accessing the Airflow UI
You can access the Airflow UI at `http://localhost:8080` using the default credentials:
- Username: `airflow`
- Password: `airflow`
