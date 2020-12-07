import os
import sys
import math

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

from logging import getLogger, INFO
from logging.handlers import TimedRotatingFileHandler


class TemperatureMetricsLogger:
    def __init__(self):
        self.log_name = 'raspiobserver_temp_metrics.csv'
        self.log_path = os.path.join('/var/tmp/', self.log_name)

        handler = TimedRotatingFileHandler(
            self.log_path,
            encoding='utf-8',
            when='midnight',
            backupCount=7,
        )
        handler.setLevel(INFO)

        self.logger = getLogger('raspiobserver_data_logger')
        self.logger.setLevel(INFO)
        self.logger.addHandler(handler)

    def log(self, data):
        csv_line = self.convert_data_to_csv(data)
        self.logger.info(csv_line)

    def convert_data_to_csv(self, data):
        return ','.join([
            f"\"{data['hostname']}\"",
            f"\"{data['created_date']}\"",
            f"\"{data['created_at']}\"",
            f"\"{data['temperature']}\"",
            f"\"{data['humidity']}\"",
            f"\"{data['airpressure']}\"",
            f"\"{data['cpu_temp']}\"",
        ])


class HardwareMetricsLogger:
    def __init__(self):
        self.log_name = 'raspiobserver_hw_metrics.csv'
        self.log_path = os.path.join('/var/tmp/', self.log_name)

        handler = TimedRotatingFileHandler(
            self.log_path,
            encoding='utf-8',
            when='midnight',
            backupCount=7,
        )
        handler.setLevel(INFO)

        self.logger = getLogger(__name__)
        self.logger.setLevel(INFO)
        self.logger.addHandler(handler)

    def log(self, data):
        csv_line = self.convert_data_to_csv(data)
        self.logger.info(csv_line)

    def convert_data_to_csv(self, data):
        return ','.join([
            f"\"{data['hostname']}\"",
            f"\"{data['created_date']}\"",
            f"\"{data['created_at']}\"",
            f"\"{data['cpu_temp']}\"",
            f"\"{data['cpu_clock']}\"",
            f"\"{data['cpu_volts']}\"",
            f"\"{to_mb(data['cpu_mem'])}\"",
            f"\"{to_mb(data['memory_total'])}\"",
            f"\"{to_mb(data['memory_used'])}\"",
            f"\"{to_mb(data['memory_free'])}\"",
            f"\"{to_mb(data['disk_total'])}\"",
            f"\"{to_mb(data['disk_used'])}\"",
            f"\"{to_mb(data['disk_free'])}\"",
        ])


#def to_mb(x, n=2):
#    x = x / 1024 / 1024
#    return math.floor(x * 10 ** n) / (10 ** n)
def to_mb(x):
    return math.floor(x / 1024 / 1024)



if __name__ == '__main__':
    import applib.data_helper

    data = applib.data_helper.get_all()

    #logger = TemperatureMetricsLogger()
    logger = HardwareMetricsLogger()
    logger.log(data)

