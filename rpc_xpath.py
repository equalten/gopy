# xpath를 이용해서 xml의 특정 위치의 값을 가져오기

from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per', normalize=True) as dev:
#    rsp = dev.rpc.get_interface_information(interface_name='xe-2/0/0', terse=True)
    rsp = dev.rpc.get_interface_information(terse=True)
#    print(etree.tostring(rsp, encoding='unicode', pretty_print=True))
#    print("#################")
    i = 0
    while True:
        print(rsp.xpath(".//address-family[address-family-name='inet']/interface-address/ifa-local")[i].text)
        i += 1
        

