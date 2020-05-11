FROM python:3.7.6-slim

ENV PACKAGES="\
    build-essential \
    ca-certificates \
    ffmpeg \
"

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

RUN apt-get update \
    && apt-get install -y --no-install-recommends $PACKAGES \
    && pip install --upgrade pip

VOLUME /tmp

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY ktv /ktv

ENTRYPOINT ["tini", "-g", "--"]
CMD ["python", "-m", "ktv"]
