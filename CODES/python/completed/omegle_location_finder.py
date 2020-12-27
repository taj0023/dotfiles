#!/usr/bin/env python3
import subprocess as sub
from geolite2 import geolite2

noice = sub.Popen('tshark', stdout=sub.PIPE, stderr=sub.STDOUT)
reader = geolite2.reader()
nice_ips = ['104.23.139.25', '192.168.29.87',
            '162.159.136.234', '104.23.143.25']


def get_location(ip):
    location = reader.get(ip)
    try:
        country = location['country']['names']['en']
    except:
        country = "Unknown"

    try:
        city = location['city']['names']['en']
    except:
        city = "Unknown"

    return country, city


for line in iter(noice.stdout.readline, b""):
    columns = line.decode().split()

    if "→" in columns:
        ip = columns[columns.index("→")-1]

        if ip in nice_ips:
            continue
        else:
            try:
                co, ci = get_location(ip)
                print(
                    f"Country: {co.ljust(15)}| City: {ci.ljust(10)} | IP: {ip}")
            except:
                pass
