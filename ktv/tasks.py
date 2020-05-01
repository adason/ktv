from pathlib import Path
import logging

import ffmpeg
from spleeter.separator import Separator
import youtube_dl

import ktv.constants as const


logger = logging.getLogger(__name__)


def download(url, filename):
    filename_ext = f"{filename}.{const.VIDEO_EXTENSION}"
    ydl_opts = {
        "format": (
            f"bestvideo[ext={const.VIDEO_EXTENSION}]+"
            f"bestaudio[ext={const.AUDIO_EXTENSION}]/best"
        ),
        "logger": logger,
        "outtmpl": filename_ext
    }

    logger.info(f"Downloading from {url} and save into {filename_ext}")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        retcode = ydl.download([url])

    logger.debug(f"Download retcode {retcode}")

    return retcode


def extract_audio(filename):
    in_video = f"{filename}.{const.VIDEO_EXTENSION}"
    out_audio = f"{filename}.{const.AUDIO_EXTENSION}"
    ffmpeg.input(in_video).output(out_audio).overwrite_output().run()


def split(filename):
    filename_ext = f"{filename}.{const.AUDIO_EXTENSION}"
    separator = Separator("spleeter:2stems")
    logger.info(f"Splitting file {filename_ext}")
    separator.separate_to_file(filename_ext, Path(filename).parent)


def combine(filename):
    in_video = f"{filename}.{const.VIDEO_EXTENSION}"
    out_video = f"{filename}_processed.{const.VIDEO_EXTENSION}"
    vocals = str(Path(filename) / "vocals.wav")
    accompaniment = str(Path(filename) / "accompaniment.wav")
    combined = ffmpeg.output(
        ffmpeg.input(in_video),
        ffmpeg.input(accompaniment),
        ffmpeg.input(vocals),
        filename=out_video
    )
    combined.overwrite_output().run()


