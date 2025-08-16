# Sample Docker Push Application

This is a sample application that demonstrates how to build a Docker image for a Python web application and push it to Docker Hub.

## Prerequisites

- Docker installed and running.
- Python 3.9+ installed.
- `uv` package manager installed.

## Setup

1.  Install the required Python packages:
    ```bash
    uv pip install -r requirements.txt
    ```

## Running the Application Locally

1.  Start the application using uvicorn:
    ```bash
    uvicorn main:app --reload
    ```
2.  Open your browser and navigate to `http://127.0.0.1:8000`.

## Building and Pushing the Docker Image

1.  Make the `ci.py` script executable:
    ```bash
    chmod +x ci.py
    ```
2.  Run the script to build and push the image. Replace `my-app` with your desired image name.
    ```bash
    ./ci.py build-and-push --image-name my-app
    ```
    This will build the image as `b8kings0ga/my-app` and push it to Docker Hub. You will need to be logged into Docker Hub for the push to succeed.