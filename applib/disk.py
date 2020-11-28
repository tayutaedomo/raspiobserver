import psutil


def get_total():
    usage = get_disk_usage()
    return usage.total


def get_used():
    usage = get_disk_usage()
    return usage.used


def get_free():
    usage = get_disk_usage()
    return usage.free


def get_disk_usage():
    return psutil.disk_usage('/')


def get_disk_partitions():
    return psutil.disk_partitions()



if __name__ == '__main__':
    print('Total:', get_total())
    print('Used: ', get_used())
    print('Free: ', get_free())

    print('Usage:', get_disk_usage())
    print('Partition:', get_disk_partitions())

