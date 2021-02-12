# YANG model not working... 추가 확인 필요함 

from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    #config_data = dev.rpc.get_config(filter_xml='bgp', model='openconfig')
    config_data=dev.rpc.get_config(filter_xml='protocols/bgp', model='openconfig', remove_ns=False)
    #config_data=dev.rpc.get_config(filter_xml='protocols/bgp')
    print(etree.tostring(config_data, encoding='unicode', pretty_print=True))