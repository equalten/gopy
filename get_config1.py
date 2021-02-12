# XML 형태로 config 가져오기

from jnpr.junos import Device
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
#    conf = dev.rpc.get_config() # candidate configuration
#    conf = dev.rpc.get_config(options = {'database':'committed', 'format':'text'}) # committed config를 text로 받기
    conf = dev.rpc.get_config(options = {'database':'committed'}) # committed config를 XML로 받기
    print(etree.tostring(conf, encoding='unicode', pretty_print=True))