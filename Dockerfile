FROM python:3.7.6-slim

ENV PACKAGES="\
    build-essential \
    ca-certificates \
    ffmpeg \
"

RUN apt-get update \
    && apt-get install -y --no-install-recommends $PACKAGES \
    && pip install --upgrade pip

VOLUME /tmp

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY ktv /ktv

ENTRYPOINT ["python", "-m", "ktv"]
