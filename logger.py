import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.INFO)
FORMAT = '%(levelname)s: "%(pathname)s", line %(lineno)s: %(funcName)s() -> %(message)s'
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)
