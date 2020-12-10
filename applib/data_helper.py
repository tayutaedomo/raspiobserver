import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

from datetime import datetime

import applib.sensehat
import applib.cpu
import applib.memory
import applib.disk


def get_all():
    data = {}

    data.update(get_hostname())
    data.update(get_date())
    data.update(get_senshat())
    data.update(get_cpu())
    data.update(get_memory())
    data.update(get_disk())

    return data

def get_hostname():
    return {'hostname': os.uname()[1]}

def get_date():
    now = datetime.now()

    return {
        'created_date': str(now.date()),
        'created_at': now.isoformat(),
    }

def get_senshat():
    try:
        compass = applib.sensehat.get_compass_raw()
        gyroscope = applib.sensehat.get_gyroscope_raw()
        accelero = applib.sensehat.get_accelerometer_raw()

        return {
            'temperature': applib.sensehat.get_temperature(),
            'humidity': applib.sensehat.get_humidity(),
            'airpressure': applib.sensehat.get_pressure(),
            'compass_x': compass['x'],
            'compass_y': compass['y'],
            'compass_z': compass['z'],
            'gyroscope_x': gyroscope['x'],
            'gyroscope_y': gyroscope['y'],
            'gyroscope_z': gyroscope['z'],
            'accelero_x': accelero['x'],
            'accelero_y': accelero['y'],
            'accelero_z': accelero['z'],
        }
    except:
        return {
            'temperature': None,
            'humidity': None,
            'airpressure': None,
            'compass_x': None,
            'compass_y': None,
            'compass_z': None,
            'gyroscope_x': None,
            'gyroscope_y': None,
            'gyroscope_z': None,
            'accelero_x': None,
            'accelero_y': None,
            'accelero_z': None,
        }


def get_cpu():
    return {
        'cpu_temp': applib.cpu.get_temp(),
        'cpu_clock': applib.cpu.get_clock(),
        'cpu_volts': applib.cpu.get_volts(),
        'cpu_mem': applib.cpu.get_memory()
    }


def get_memory():
    return {
        'memory_total': applib.memory.get_total(),
        'memory_used': applib.memory.get_used(),
        'memory_free': applib.memory.get_free(),
    }


def get_disk():
    return {
        'disk_total': applib.disk.get_total(),
        'disk_used': applib.disk.get_used(),
        'disk_free': applib.disk.get_free(),
    }



if __name__ == '__main__':
    print(get_all())

