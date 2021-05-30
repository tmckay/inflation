#/bin/bash

docker build --tag inflation . 2> /dev/null
docker run --rm -it inflation "$@" 
