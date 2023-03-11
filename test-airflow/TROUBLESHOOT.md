# Airflow Troubleshooting Guide

This guide outlines common issues encountered while using Airflow and provides potential solutions to help diagnose and resolve problems.

## Common Issues and Solutions

### DAGs not showing up in Airflow Web UI

**Issue:** DAG files may not be placed in the correct directory.

**Solution:** Confirm that DAG files are placed in the `dags_folder` directory specified in the Airflow configuration file (by default, this is `/usr/local/airflow/dags`). If the `dags_folder` location is changed, verify that the updated location is properly reflected in the Airflow configuration file.

**Issue:** DAG files may not follow the correct naming conventions.

**Solution:** Confirm that DAG files follow the naming convention of `example_dag.py` and that they contain a `dag` object that is properly defined.

**Issue:** The `airflow scheduler` and/or `airflow webserver` commands may not be running.

**Solution:** Run the `airflow scheduler` and `airflow webserver` commands in separate terminal windows to start the scheduler and webserver processes. If either process stops or crashes, check the logs to identify the cause of the issue.

### Task Instances are stuck in "running" state

**Issue:** The task instance may be stuck due to a worker process that has crashed or is otherwise unavailable.

**Solution:** Check the logs for the task instance to identify any errors that occurred during task execution. If the worker process is not available, try restarting the worker process and re-running the task.

**Issue:** The task instance may be waiting for external resources to become available.

**Solution:** Check the task dependencies to identify any external dependencies that may be causing the task instance to wait. If external dependencies are the issue, consider adjusting the dependencies or increasing the timeout value for the task.

## Troubleshooting Checklist

When encountering issues with Airflow, it's helpful to follow a checklist to help identify and resolve issues. Here are some common steps to take when troubleshooting Airflow:

1. Check the Airflow logs for errors and warnings.

    ```shell
    $ docker exec -it <container_name> bash
    $ cd /usr/local/airflow/logs/
    $ tail <log_filename>
    ```

2. Check the Airflow webserver to confirm that DAGs are available and running.

    ```shell
    $ docker exec -it <container_name> bash
    $ airflow dags list
    $ airflow tasks list <dag_id>
    ```

3. Check the Airflow scheduler to confirm that it is running.

    ```shell
    $ docker exec -it <container_name> bash
    $ ps -ef | grep airflow
    ```

4. Confirm that DAGs are placed in the correct directory and follow the naming convention of `example_dag.py`.

    ```shell
    $ docker exec -it <container_name> bash
    $ cd /usr/local/airflow/dags/
    $ ls
    ```

5. Confirm that Airflow configuration settings are set correctly and that the `airflow.cfg` file is in the correct location.

    ```shell
    $ docker exec -it <container_name> bash
    $ cd /usr/local/airflow/
    $ cat airflow.cfg
    ```

