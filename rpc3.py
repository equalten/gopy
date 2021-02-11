from jnpr.junos import Device
from lxml import etree
import xml.dom.minidom

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per')

dev.open()

inter_info = dev.rpc.get_interface_information()
dom = xml.dom.minidom.parse(inter_info)
print(dom.toprettyxml())

dev.close()
