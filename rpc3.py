from jnpr.junos import Device
from lxml import etree
import xml.dom.minidom

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per')

dev.open()

inter_info = dev.rpc.get_interface_information()
print(etree.tostring(inter_info, encoding='utf8', method='xml', xml_declaration=True))
dev.close()
