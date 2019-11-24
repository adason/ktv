import logging

import youtube_dl

logger = logging.getLogger(__name__)


def download(url, output):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "logger": logger,
        "outtmpl": output + ".%(ext)s"
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        retcode = ydl.download([url])

    return retcode

