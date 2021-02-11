from jnpr.junos import Device
from lxml import etree


with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    sw_version = dev.rpc.get_software_information()
    print(etree.tostring(sw_version))

    inter_info = dev.rpc.get_interface_information(terse=True)
    print(etree.tostring(inter_info))

    inter_info_0 = dev.rpc.get_interface_information(interface_name = 'xe-2/0/0')
    print(etree.tostring(inter_info_0))