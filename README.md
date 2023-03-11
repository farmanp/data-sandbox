# Data Engineering Sandbox

This is a project for testing and exploring various data engineering tools and technologies. The project is organized as a Python package that includes subdirectories for each technology being tested.

## Technologies

The following technologies are currently being tested:

- Apache Airflow
- Apache Beam
- Apache Flink
- Elasticsearch
- Kafka
- Kibana
- Logstash

Each technology has its own directory under the `test-technology` naming convention. Inside each directory, there is a `main.py` file that can be used to test and experiment with the technology.

## Installation

To install the project dependencies, use the following command:

```
poetry install
```


This will create a virtual environment and install all the required dependencies specified in the `pyproject.toml` file.

## Usage

To use the project, activate the virtual environment using the following command:

```
poetry shell
```


You can then navigate to the directory for the technology you want to test and run the `main.py` file to experiment with the technology.

## Contributing

Contributions to the project are welcome! If you find a bug or have a suggestion for a new technology to test, please create a GitHub issue to discuss.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
