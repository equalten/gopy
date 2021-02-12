# ethernet interface 상태 table

from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortErrorTable
from lxml import etree
from pprint import pprint

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    eth = PhyPortErrorTable(dev)
    eth_stat = eth.get()

    for item in eth_stat:
        print(eth_stat)
