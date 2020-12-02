import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

from logging import getLogger, INFO
from logging.handlers import TimedRotatingFileHandler


class DataLogger:
    def __init__(self):
        self.log_name = 'raspiobserver_data.csv'
        self.log_path = os.path.join('/var/tmp/', self.log_name)

        handler = TimedRotatingFileHandler(
            self.log_path,
            encoding='utf-8',
            when='D',
            interval=1,
            backupCount=7,
        )
        handler.setLevel(INFO)

        self.logger = getLogger('raspiobserver_data_logger')
        self.logger.setLevel(INFO)
        self.logger.addHandler(handler)

    def log(self, data):
        csv_line = self.convert_data_to_csv(data)
        print(csv_line) # debug
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
            f"\"{data['cpu_clock']}\"",
            f"\"{data['cpu_volts']}\"",
        ])



if __name__ == '__main__':
    import applib.data_helper

    data = applib.data_helper.get_all()

    logger = DataLogger()
    logger.log(data)

