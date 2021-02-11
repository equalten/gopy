from jnpr.junos import Device
from lxml import etree

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per')

dev.open()

sw_version_text = dev.rpc.get_software_information({'format':'text'})
print(etree.tostring(sw_version))

sw_version_json = dev.rpc.get_software_information({'format':'json'})
pprint(sw_version_json)

dev.close()