FROM python:3.8-slim-buster

# Set environment variables
ENV AIRFLOW_HOME=/usr/local/airflow
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/airflow"

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get install -y --no-install-recommends libffi-dev && \
    apt-get install -y --no-install-recommends libssl-dev && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Airflow
ARG AIRFLOW_VERSION=2.2.3
RUN pip install --no-cache-dir "apache-airflow[${AIRFLOW_EXTRAS}]==${AIRFLOW_VERSION}"

# Copy requirements.txt file
COPY requirements.txt /tmp/requirements.txt

# Install additional packages from requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy DAGs
COPY ./dags /usr/local/airflow/dags

# Copy airflow.cfg file
COPY ./config/airflow.cfg /usr/local/airflow/airflow.cfg

# Initialize Airflow database
RUN airflow db init
RUN airflow users create --role Admin --username admin --email admin@example.com --firstname Admin --lastname User --password admin

# Expose ports
EXPOSE 8080

# Start Airflow webserver and scheduler
CMD ["bash", "-c", "airflow webserver & airflow scheduler"]
