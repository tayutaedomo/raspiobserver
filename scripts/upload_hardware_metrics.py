#!/usr/bin/env python3
import os
import sys
from datetime import date, timedelta

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))


from applib.uploader import HardwaerMetricsLogUploader


if __name__ == '__main__':
    target_date = str(date.today() - timedelta(days=1))

    if len(sys.argv) > 1:
        target_date = sys.argv[1]

    uploader = HardwaerMetricsLogUploader()
    uploader.upload(target_date)

