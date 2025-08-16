# Plan for tapp Application and CI Pipeline

This document outlines the plan for the "Echo App" sample application and its Continuous Integration (CI) pipeline using GitHub Actions.

## 1. Echo App Architecture

The "Echo App" will be a simple web application built with Python and Flask. Its primary function is to echo back any message it receives via a POST request to the `/echo` endpoint.

### Key Components:

*   **Backend:** A lightweight Flask application that exposes a single API endpoint (`/echo`).
*   **Containerization:** The application will be containerized using Docker. A `Dockerfile` will be created to define the application image.
*   **Configuration:** Application configuration (e.g., port) will be managed through environment variables.

## 2. GitHub Actions CI Pipeline Stages

The CI pipeline will be defined in a GitHub Actions workflow file (`.github/workflows/ci.yml`). The pipeline will be triggered on every push to the `main` branch.

### Stages:

1.  **Checkout:** The first step will be to check out the source code from the repository.
2.  **Set up Build Environment:** Set up the necessary environment, including Python and Docker.
3.  **Lint & Test:** Run static analysis (e.g., `flake8`) and unit tests (e.g., `pytest`) to ensure code quality.
4.  **Build Docker Image:** Build the Docker image for the application using the `Dockerfile`.
5.  **Publish Docker Image:**
    *   Log in to a container registry (e.g., GitHub Container Registry - GHCR).
    *   Tag the Docker image with a version number.
    *   Push the tagged image to the container registry.
6.  **Trigger tgitops Update:** The final step will trigger an update in the `tgitops` repository.

## 3. Docker Image Versioning Strategy

A simple and effective versioning strategy will be used for the Docker images.

*   **Versioning Scheme:** Images will be tagged with the Git commit SHA. For example: `ghcr.io/user/tapp:<git-sha>`.
*   **Rationale:** Using the Git SHA provides a direct link between the container image and the exact version of the source code that produced it. This ensures traceability and reproducibility. A `latest` tag will also be pushed to point to the most recent build from the `main` branch.

## 4. Mechanism for Updating tgitops Repository

To achieve GitOps, the CI pipeline in `tapp` needs to automatically update the Kubernetes manifests in the `tgitops` repository.

### Mechanism:

1.  **Personal Access Token (PAT):** A GitHub Personal Access Token (PAT) with `repo` scope will be created and stored as a secret in the `tapp` repository (e.g., `T_GITOPS_PAT`).
2.  **Checkout tgitops:** The CI workflow will use this PAT to check out the `tgitops` repository into a separate directory.
3.  **Update Manifest:** The workflow will use a tool like `sed` or `yq` to update the image tag in the relevant Kubernetes deployment manifest (e.g., `tgitops/app/deployment.yaml`) with the new Git SHA-based tag.
4.  **Commit and Push:** The workflow will commit the change to the manifest file and push it back to the `tgitops` repository. This push will trigger Argo CD (or a similar GitOps tool) to deploy the new version of the application.

This automated update process ensures that the state of the production environment (defined in `tgitops`) is always in sync with the latest successful build of the application (`tapp`).