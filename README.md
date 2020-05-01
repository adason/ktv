# KTV
Split vocal and accompaniment for a given youtube URL.

## Download and split using docker

For example, to split this [song](https://www.youtube.com/watch?v=51SOZjKuaaQ)

```
docker run \
  -e MODEL_PATH=/tmp/ktv/models \
  -v /tmp:/tmp \
  -t adason/ktv:latest \
  -o luggage \
  https://www.youtube.com/watch?v=51SOZjKuaaQ
```

You can find downloaded mp3 file as well as split files under `/tmp/ktv`.

## Development

### Python virtualenv

```
python -m ktv -o output https://www.youtube.com/watch?v=VpwAq7hiij0
```

### Docker

```
docker build -t ktv .

docker run \
  -e MODEL_PATH=/tmp/ktv/models \
  -v /tmp:/tmp \
  -t ktv \
  -o luggage \
  https://www.youtube.com/watch?v=51SOZjKuaaQ
```

Push to docker registry
```
docker tag ktv adason/ktv:latest
docker push adason/ktv:latest
```
