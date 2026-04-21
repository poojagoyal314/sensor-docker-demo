# Sensor Docker Demo

![CI Pipeline](https://github.com/poojagoyal314/sensor-docker-demo/actions/workflows/ci.yml/badge.svg)

A containerised signal processing pipeline with automated CI — built with Docker and GitHub Actions.

## What it does
Applies a Butterworth low-pass filter to a simulated MEMS sensor signal (1kHz, 10Hz sine + noise).
Two services run via docker-compose: a data generator and the signal processor.

## Run it instantly — no local dependencies needed
```bash
docker pull poojagoyal314/sensor-docker-demo
docker run poojagoyal314/sensor-docker-demo
```

## Run with docker-compose
```bash
docker compose up
```

## Stack
- Python 3.11-slim
- NumPy, SciPy
- Docker + docker-compose
- GitHub Actions CI