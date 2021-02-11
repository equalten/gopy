from jnpr.junos import Device
from lxml import etree

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per')

dev.open()
print(dev.display_xml_rpc('show route', format='text'))
route = dev.rpc.get_route_information()
print(etree.tostring(route, encoding='unicode'))
dev.close()
