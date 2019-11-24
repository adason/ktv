import argparse
import logging

from ktv.grab import download

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
    parser.add_argument("url", type=str, help="a youtube url")
    parser.add_argument("-o", "--output", type=str, help="output filename")

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
    output = args.output
    retcode = download(url, output)
    logger.debug(retcode)


if __name__ == "__main__":
    main()
