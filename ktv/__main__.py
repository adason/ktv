import argparse
import logging
from pathlib import Path

from ktv.tasks import download, split
import ktv.constants as const


FORMAT = "%(asctime)-15s | %(module)s | %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert youtube video to vocal and audio tracks"
    )
    parser.add_argument(
        "-v", "--vervbose", action="store_true", default=False, help="debug mode"
    )
    parser.add_argument(
        "-o", "--output", type=str, default=const.FILENAME,
        help="output filename (exclude extension)"
    )
    parser.add_argument("url", type=str, help="a youtube url")

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    root_logger = logging.getLogger()
    if args.vervbose:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(logging.INFO)

    logger.debug(args)

    url = args.url
    out_file_ext = args.output + const.EXTENSION
    output = str(Path(const.OUTPUT_DIR) / out_file_ext)
    download(url, output)
    split(output)


if __name__ == "__main__":
    main()
