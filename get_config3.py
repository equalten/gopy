from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from lxml import etree
import sys

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per')

try:
    dev.open()

    filter='<configuration><interfaces/><protocols/></configuration>'
    data = dev.rpc.get_config(filter_xml=filter)
    print(etree.tostring(data, encoding='unicode', pretty_print=True))
    input("Press 'Enter' to continue: ")

    data = dev.rpc.get_config(filter_xml='<system><services/></system>')
    print(etree.tostring(data, encoding='unicode', pretty_print=True))
    input("Press 'Enter' to continue: ")

    data = dev.rpc.get_config(filter_xml='system/services')
    print(etree.tostring(data, encoding='unicode', pretty_print=True))
    input("Press 'Enter' to continue: ")

    filter=etree.XML('<system><services/></system>')
    data = dev.rpc.get_config(filter_xml=filter)
    print(etree.tostring(data, encoding='unicode', pretty_print=True))
    dev.close()



except ConnectError as err:
    print("Cannot connect to device: {0}".format(err)) 
    sys.exit(1)
except Exception as err:
    print(err)
    sys.exit(1)
