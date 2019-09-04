#!/usr/bin/env bash

set -e

CONTAINER_TAG=htmap-workshop

docker build -t ${CONTAINER_TAG} --file .docker/Dockerfile .
docker run -it --rm --mount type=bind,source="$(pwd)",target=/home/me/workshop ${CONTAINER_TAG} bash
