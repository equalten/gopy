import sys
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from getpass import getpass
from pprint import pprint

hostname = input("Hostname to connect: ")
username = input("JUNOS username: ")
password = getpass("JUNOS password: ")

dev = Device(host=hostname, user=username, passwd=password, mode='telnet', port='23')

try:
    dev.open()
except Exception as err:
    print("Connection Error with {0}".format(err))
    sys.exit(1)

print(dev.facts["hostname"])
pprint(dev.facts)

dev.close()
