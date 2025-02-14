# FTP Upload and Reboot Script

This script uploads a file to a remote device via FTP and then reboots the device using SSH. It reads IP addresses from a file (`IPadres.txt`) and performs the operation on each IP address listed. This is the way to upload a new (boot) CODESYS application. Restarting the controller makes sure the new application is running.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- `ftplib` (built-in)
- `paramiko` (install via `pip install paramiko`)

## Usage

1. Prepare an `IPadres.txt` file with a list of IP addresses, one per line.
2. Place the file you want to upload in the same directory as the script.
3. Run the script:
   ```sh
   python script.py
   ```

## Docker Setup

To run the script inside a Docker container, follow these steps.

### 1. Create a `Dockerfile`

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install paramiko
CMD ["python", "script.py"]
```

### 2. Build the Docker Image

```sh
docker build -t wago-update-codesys-application .
```

### 3. Run the Docker Container

```sh
docker run --rm -v $(pwd)/IPadres.txt:/app/IPadres.txt wago-update-codesys-application .

or

docker run --rm wago-update-codesys-application
```

This command mounts the `IPadres.txt` file into the container and runs the script.

## Notes
- The script assumes default credentials (`root/wago`). Update them as necessary.
- Ensure the target devices support FTP and SSH access.
- Modify `directoryname` in the script as needed based on the target system.
