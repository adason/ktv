from pathlib import Path
import logging

from spleeter.separator import Separator
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
        "outtmpl": output
    }

    logger.info(f"Downloading from {url} and convert into {output}")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        retcode = ydl.download([url])

    logger.debug(f"Download retcode {retcode}")

    return retcode


def split(file):
    separator = Separator("spleeter:2stems")
    logger.info(f"Splitting file {file}")
    separator.separate_to_file(file, Path(file).parent)
