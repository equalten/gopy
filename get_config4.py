# configuration 중 interface 이름에 관한 부분만 가져오기
# 특정 interface의 하위 configuration만 가져오기

from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    filter = '<interfaces><interface><name/></interface></interfaces>'
#    data=dev.rpc.get_config(filter_xml=filter, options={'inherit':'inherit'})
    data=dev.rpc.get_config(filter_xml=filter)
    print(etree.tostring(data, encoding='unicode', pretty_print=True))

    # xml filter를 다른 형태로...
    data=dev.rpc.get_config(filter_xml='interfaces/interface/name')
    print(etree.tostring(data, encoding='unicode', pretty_print=True))

    filter = '<interfaces><interface><name>xe-2/0/0</name></interface></interfaces>'
    data = dev.rpc.get_config(filter_xml=filter)
    print(etree.tostring(data, encoding='unicode', pretty_print=True))
