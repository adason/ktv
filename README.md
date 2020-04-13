# KTV
Split vocal and accompaniment for a given youtube URL.

## Download and split using docker

For example, to split this [song](https://www.youtube.com/watch?v=1hI-7vj2FhE)

```
docker run \
  -e MODEL_PATH=/tmp/ktv/models \
  -v /tmp:/tmp \
  -t adason/ktv:latest \
  -o quiet \
  https://www.youtube.com/watch?v=1hI-7vj2FhE
```

You can find downloaded mp3 file as well as split files under `/tmp/ktv`.

## Development

```
docker build -t ktv .

docker run \
  -e MODEL_PATH=/tmp/ktv/models \
  -v /tmp:/tmp \
  -t ktv \
  -o quiet \
  https://www.youtube.com/watch?v=1hI-7vj2FhE
```

Push to docker registry
```
docker tag ktv adason/ktv:latest
docker push adason/ktv:latest
```
