from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
#    int_detail = dev.rpc.get_interface_information(extensive=True)
#    print(etree.tostring(int_detail, encoding='unicode', pretty_print=True))

    system_stat = dev.rpc.get_statistics_information()
    print(etree.tostring(system_stat, encoding='unicode', pretty_print=True))
