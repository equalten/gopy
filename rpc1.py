from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    sw_version = dev.rpc.get_software_information()
    print(etree.tostring(sw_version, encoding='unicode', method='xml'))
