# Test Airflow

This is a simple test project to demonstrate how to use Airflow.

## Getting Started

1. Install Docker and Docker Compose
2. Clone this repository: `git clone https://github.com/your-username/test-airflow.git`
3. Build the Docker image: `docker build -t test-airflow .`
4. Start the Docker container: `docker run -p 8080:8080 test-airflow`
5. Access the Airflow UI at `http://localhost:8080`

## Configuration

The `airflow.cfg` file in the `config` directory contains the configuration settings for Airflow. You can modify this file to change Airflow's behavior. 

## DAGs

DAGs (Directed Acyclic Graphs) are a collection of tasks that are organized in a way that reflects their dependencies. In Airflow, DAGs are defined using Python code and stored in the `dags` directory. To add a new DAG, create a new Python file in the `dags` directory and define your DAG inside it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
