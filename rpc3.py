# filter를 이용해서 filter에 적용되는 정보만 가져오기

from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per', use_filter=True) as dev:
    filter = '<interface-information><physical-interface><name></name></physical-interface></interface-information>'
    
    result = dev.rpc.get_interface_information(filter_xml=filter, normalize=True) # normalize는 indent를 정렬해서 표시
    print(etree.tostring(result, encoding='unicode', pretty_print=True)) #encoding=unicode로 해야 \n 이 동작