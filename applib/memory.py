import psutil


def get_total():
    mem = psutil.virtual_memory()
    return mem.total


def get_used():
    mem = psutil.virtual_memory()
    return mem.used


def get_free():
    mem = psutil.virtual_memory()
    return mem.available



if __name__ == '__main__':
    print('Total:', get_total())
    print('Used: ', get_used())
    print('Free: ', get_free())

