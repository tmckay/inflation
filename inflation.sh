#/bin/bash

docker build --tag inflation .
docker run --rm -it inflation "$@" 
