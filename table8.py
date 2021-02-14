### custom pyez table test
### arp table을 custom table로 가져오기

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
from lxml import etree
import yaml

yaml_data = """
---
ArpTable:
  rpc: get-arp-table-information
  item: arp-table-entry
  key: mac-address
  view: ArpView
ArpView:
  fields:
    mac_address: mac-address
    ip_address: ip-address
    interface_name: interface-name
    host: hostname
"""

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    globals().update(FactoryLoader().load(yaml.load(yaml_data)))

#    arps = dev.rpc.get_arp_table_information(no_resolve=True)
    arps = ArpTable(dev)
    arp_table = arps.get()
#    pprint(arp_table)
    print(etree.tostring(arps, endcoding='unicode', pretty_print=True))

#    print(etree.tostring(arps, encoding='unicode', pretty_print=True))
#    for arp in arps:
#        print('mac address: ', arp.mac_address)

