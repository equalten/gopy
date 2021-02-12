# ethernet interface 상태 table

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from lxml import etree

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    eth = EthPortTable(dev)
    eth_get = eth.get()

    for item in eth:
        print("{} : {}".format(item.name, item.oper))
