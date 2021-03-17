from math import ceil
from collections import namedtuple

Service = namedtuple("Service", ["offset", "frequency"])

def part_1(input):
    earliest_timestamp = int(input[0])
    services = [int(x) for x in input[1].split(",") if x != "x"]

    earliest_times = [ceil(earliest_timestamp / service) * service for service in services]

    earliest_service_time = min(earliest_times)
    earliest_service_id = services[earliest_times.index(earliest_service_time)]
    time_to_service = earliest_service_time - earliest_timestamp
    return earliest_service_id * time_to_service

def part_2(input):
    services = [Service(-idx % int(service), int(service)) for idx,service in enumerate(input[1].split(",")) if service != "x"]

    value = 0                                                                                                                                                                                                                                                              
    increment = services[0].frequency

    for service in services[1:]:
        while value % service.frequency != service.offset:
            value += increment
        increment *= service.frequency

    return value