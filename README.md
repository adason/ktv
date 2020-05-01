# KTV
Split vocal and accompaniment for a given youtube URL.

## Requirements

- [docker](https://docs.docker.com/get-docker/)

## Download Video From Youtube and Process Audio Separation

For example, to split this [song](https://www.youtube.com/watch?v=51SOZjKuaaQ) and create a processed video

```
docker run \
  -e MODEL_PATH=/tmp/ktv/models \
  -v /tmp:/tmp \
  -t adason/ktv:latest \
  -o luggage \
  https://www.youtube.com/watch?v=51SOZjKuaaQ
```

The processed output video will include 3 audio tracks:
- First audio track from the original source
- Second audio track for accompaniment only
- Third audio track for vocals only

You can find processed files such as `luggage_processed.mp4` under `/tmp/ktv/` along with other intermediate files with prefix `luggage`. You can change docker mount point to any local directory (such as `-v $HOME/Downloads:/tmp`). You can also replace the filename output prefix `luggage` as desired.

## Development

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

### Python virtualenv

```
python -m ktv -o luggage https://www.youtube.com/watch?v=51SOZjKuaaQ
```
