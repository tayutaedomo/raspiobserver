import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

import applib.gcs
from applib.data_helper import get_hostname


class TemperatureMetricsLogUploader:
    def __init__(self):
        self.log_name = 'raspiobserver_temp_metrics.csv'
        self.log_path = os.path.join('/var/tmp/', self.log_name)
        self.gcs_dir = 'temperature'

    def upload(self, target_date):
        local_path = self.log_path + '.' + target_date

        if not os.path.exists(local_path):
            raise FileNotFoundError()

        gcs_file_name = self.log_name.replace('.'+'target_date', '')
        gcs_file_name = target_date + '_' + gcs_file_name
        gcs_path = self.gcs_dir + '/' + gcs_file_name

        applib.gcs.upload(gcs_path, local_path)


class HardwaerMetricsLogUploader:
    def __init__(self):
        self.log_name = 'raspiobserver_hw_metrics.csv'
        self.log_path = os.path.join('/var/tmp/', self.log_name)
        self.gcs_dir = 'hardware'

    def upload(self, target_date):
        local_path = self.log_path + '.' + target_date

        if not os.path.exists(local_path):
            raise FileNotFoundError()

        gcs_file_name = self.log_name.replace('.'+'target_date', '')
        gcs_file_name = target_date + '_' + gcs_file_name
        gcs_dir = self.gcs_dir + '/' + get_hostname()['hostname']
        gcs_path = gcs_dir + '/' + gcs_file_name

        applib.gcs.upload(gcs_path, local_path)



if __name__ == '__main__':
    uploader = TemperatureMetricsLogUploader()
    uploader.upload('2020-12-06')

