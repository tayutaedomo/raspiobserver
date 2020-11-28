import subprocess

def get_temp():
    return float(get_temp_raw().replace("'", '').replace('C', ''))


def get_temp_raw():
    return run_shell_command('vcgencmd measure_temp')


def get_clock():
    return int(get_clock_raw())


def get_clock_raw():
    return run_shell_command('vcgencmd measure_clock arm')


def get_volts():
    return float(get_volts_raw().replace('V', ''))


def get_volts_raw():
    return run_shell_command('vcgencmd measure_volts')


def get_memory():
    return int(get_memory_raw().replace('M', ''))


def get_memory_raw():
    return run_shell_command('vcgencmd get_mem arm')


#def get_gpu_memory():
#    return run_shell_command("vcgencmd get_mem gpu")


def run_shell_command(command_str):
    proc = subprocess.run(command_str, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    result = proc.stdout.split("=")
    return result[1].replace('\n', '')



if __name__ == '__main__':
    print('Temperature:', get_temp())
    print('Temperature:', get_temp_raw())
    print('Clock:      ', get_clock())
    print('Clock:      ', get_clock_raw())
    print('Volts:      ', get_volts())
    print('Volts:      ', get_volts_raw())
    print('Memory:     ', get_memory())
    print('Memory:     ', get_memory_raw())

