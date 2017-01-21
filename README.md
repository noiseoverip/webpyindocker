# Build container image
`docker build -t pythonrun .`

# Run Django server
`python manager.py runserver`

# Run python code in container:
`open http://127.0.0.1:8000`

# Tested with:
* Django: 1.9.5
* Docker version 1.12.5, build 7392c3b
* Python 3.5.2
* Ubuntu 14.04.5 LTS