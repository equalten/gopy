# configuration을 다음과 같은 다양한 format으로 가져오기
# XML, text, set, json

from jnpr.junos import Device
from lxml import etree
from pprint import pprint

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:

    # XML로 가져오기
    #config_data = dev.rpc.get_config()
    #print(etree.tostring(config_data, encoding='unicode', pretty_print=True))

    # Text로 가져오기
    #config_data = dev.rpc.get_config(options={'format':'text'})
    #print(etree.tostring(config_data, encoding='unicode', pretty_print=True))

    # set 형태로 가져오기
    #config_data = dev.rpc.get_config(options={'format':'set'})
    #print(etree.tostring(config_data, encoding='unicode', pretty_print=True))

    # JSON 형태로 가져오기
    config_data = dev.rpc.get_config(options={'format':'json'})
    pprint(config_data)