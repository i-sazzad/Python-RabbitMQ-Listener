import re
import sys
import os
import logging
import datetime
import random
import calendar
from calendar import monthrange
logging.basicConfig(filename=f"debug/{datetime.date.today()}.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def print_error(error):
    error = get_error_message(error)
    logging.warning(error)
    raise


def print_error_info(error):
    error = get_error_message_with_path(error)
    error = get_error_message(error)
    logging.warning(error)


def print_debug(message):
    logging.debug(str(message))


def print_info(message):
    logging.info(str(message))
