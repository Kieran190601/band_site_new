# Project Name

## Setup Instructions

### Using Virtual Environment
1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
3. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

### Using Docker
1. Build the Docker image:
    ```bash
    docker build -t project_name .
    ```
2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 project_name
    ```

## Usage
This is used  to run a server that displays a bands information
