from jnpr.junos import Device

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per')

dev.open()
print(dev.display_xml_rpc('show route', format='text'))
route = dev.rpc.get_route_information()
print(route)
dev.close()
