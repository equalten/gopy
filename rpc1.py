from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    sw_version = dev.rpc.get_software_information()
    for item in etree.tostring(sw_version):
        print(item)
        