# RPC method를 이용해서 cli output 정보 가져오기
# terse, interface_name 등 옵션 주는 방법 확인

from jnpr.junos import Device
from lxml import etree


with Device(host='172.27.14.72', user='jun', passwd='jun2per', normalize=True) as dev:
    sw_version = dev.rpc.get_software_information()
    print(etree.tostring(sw_version, encoding='unicode', pretty_print=True))

    inter_info = dev.rpc.get_interface_information(terse=True)
    print(etree.tostring(inter_info, encoding='unicode', pretty_print=True))

    inter_info_0 = dev.rpc.get_interface_information(interface_name = 'xe-2/0/0')
    print(etree.tostring(inter_info_0, encoding='unicode', pretty_print=True))