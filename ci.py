#!/opt/homebrew/bin/uv run -q --script
# /// script
# name = "ci"
# dependencies = [
#    "typer",
# ]
# ///

import typer
import subprocess

app = typer.Typer()

@app.command()
def build_and_push(image_name: str, username: str = "b8kings0ga"):
    """
    Builds and pushes a Docker image.
    """
    try:
        # Build the Docker image
        build_command = ["docker", "build", "-t", f"{username}/{image_name}", "."]
        print(f"Running command: {' '.join(build_command)}")
        subprocess.run(build_command, check=True)

        # Push the Docker image
        push_command = ["docker", "push", f"{username}/{image_name}"]
        print(f"Running command: {' '.join(push_command)}")
        subprocess.run(push_command, check=True)

        print(f"Successfully built and pushed {username}/{image_name}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print("Docker is not installed or not in the system's PATH.")

if __name__ == "__main__":
    app()