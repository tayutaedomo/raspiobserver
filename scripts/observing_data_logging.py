#!/usr/bin/env python3
import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

from applib import data_helper
from applib.observer_logger import DataLogger


if __name__ == '__main__':
    data = data_helper.get_all()

    logger = DataLogger()
    logger.log(data)

