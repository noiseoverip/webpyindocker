#!/usr/bin/env bash
# Wrapper for executing python script inside docker container
#
# Make sure your user is in docker group so you can run this
# Add your user to docker group: sudo usermod -aG docker $USER
#
# Example usage ./runInContainer.sh myscript.py

script=$1
docker run --rm -v "$PWD/"$script:/root/script.py pythonrun python /root/script.py