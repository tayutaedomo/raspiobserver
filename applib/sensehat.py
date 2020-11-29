from sense_hat import SenseHat


def get_temperature():
    sense = SenseHat()
    #return sense.get_temperature_from_humidity()
    return sense.get_temperature_from_pressure()


def get_humidity():
    sense = SenseHat()
    return sense.get_humidity()


def get_pressure():
    sense = SenseHat()
    return sense.get_pressure()


def get_compass_raw():
    sense = SenseHat()
    sense.set_imu_config(True, False, False) # Compass only
    return sense.get_compass_raw()


def get_gyroscope_raw():
    sense = SenseHat()
    sense.set_imu_config(False, True, False) # Gyroscope only
    return sense.get_gyroscope_raw()


def get_accelerometer_raw():
    sense = SenseHat()
    sense.set_imu_config(False, False, True) # Accelerometer only
    return sense.get_accelerometer_raw()



if __name__ == '__main__':
    print('Temperature:  ', get_temperature())
    print('Humidity:     ', get_humidity())
    print('Air pressure: ', get_pressure())

    print('Compass:      ', get_compass_raw())
    print('Gyroscope:    ', get_gyroscope_raw())
    print('Accelerometer:', get_accelerometer_raw())

