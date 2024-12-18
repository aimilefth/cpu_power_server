# Power Metrics Flask Server

This project provides a simple Flask server that returns CPU power metrics from `pyJoules`. The server is containerized using Docker.

## Project Structure

```

.
├── code
│   ├── flask_server.py
│   └── power_scraper.py
├── docker
│   └── Dockerfile
└── README.md

````

- **code/flask_server.py** : The main Flask application that defines a `/api/cpu_power` endpoint.
- **code/power_scraper.py** : A helper module using `pyJoules` to measure CPU energy usage.
- **docker/Dockerfile** : Dockerfile to build the container.

## Prerequisites

- **Docker** installed on your system.

## Build the Docker Image

1. Navigate to the root directory of this project (the directory containing `docker/` and `code/`).
2. Run the Docker build command, specifying the Dockerfile location:

   ```bash
   docker build -t power-metrics -f docker/Dockerfile .
   ```

    This will:

    - Pull the Python 3.12 slim base image,
    - Copy the `code/` directory,
    - Install necessary Python dependencies (`pyJoules`, `requests`, `flask`),
    - Expose port 5000,
    - Specify the startup command (`CMD`).

## Run the Docker Container

After the image is built, you can run a container:

```bash
docker run -d --privileged -p 5000:5000 --network=host power-metrics
```

- `-d` runs the container in the background (detached).
- `-p 5000:5000` maps host port 5000 to container port 5000.
- `--name power-metrics-container` sets a friendly container name.

If you want to override the default port, you can set the `PORT` environment variable:

```bash
docker run -d --privileged  -p 8080:8080 -e PORT=8080 --network=host power-metrics
```

Now, the Flask server will listen on port `8080` inside the container, and the host machine will map `8080` to the container port.

## Testing the Endpoint

You can test the `/api/cpu_power` endpoint using `curl` or any REST client:

```bash
curl -X POST http://localhost:5000/api/cpu_power

# or, if you used a custom port (say 8080):
curl -X POST http://localhost:8080/api/cpu_power
```

You should receive a JSON response with power metrics like:

```json
{
  "timestamp": 1672839007.12345,
  "tag": "waste_time_sleep",
  "duration": 0.1,
  "package_0": <energy value>,
  "dram_0": <energy value>,
  ...
}
```

## Environment Variables

- **DEVICE\_ID**: If needed for your environment, set this when running the container using `-e DEVICE_ID=<id>`; the `power_scraper.py` uses this to build commands for measuring power on a specific device (default is `"0"`).
- **PORT**: Specify which port Flask should listen on (default is `5000`).

---

### Notes & Tips

1. **Device ID**: Since your `power_scraper` class constructor requires a `device_id`, you should either provide it explicitly or let it default to `'0'`. If you truly need a dynamic device ID, you can pass it as an environment variable at runtime via `-e DEVICE_ID=<id>`.
2. **Debugging**: If you encounter any issues with `pyJoules`, ensure your hardware and OS are supported. You may also need privileges or special environment settings for hardware-level measurement.
3. **Logs**: You can view the container logs via `docker logs power-metrics-container` for troubleshooting.

With these changes and instructions, you should have a fully working Flask server Docker image that can be built and run successfully.

**Enjoy measuring power metrics with your Flask application!**