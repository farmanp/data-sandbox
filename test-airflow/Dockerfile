FROM python:3.8-slim-buster

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Airflow and its dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy DAGs and other configuration files
# COPY dags/ /usr/local/airflow/dags/
# COPY config/ /usr/local/airflow/config/

# Expose port 8080
EXPOSE 8080

# Initialize Airflow database
RUN airflow db init
RUN airflow users create --role Admin --username admin --email admin@example.com --firstname Admin --lastname User --password admin
# Set the working directory
WORKDIR /usr/local/airflow

# Start the webserver and scheduler
CMD ["bash", "-c", "airflow webserver & airflow scheduler"]
