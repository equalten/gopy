# EthPortTable을 이용한 ethernet interface 상태 확인

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from lxml import etree
from pprint import pprint

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    eth = EthPortTable(dev)
    eth_get = eth.get()

    #print(eth.keys())
    #pprint(eth.values())
    pprint(eth.items())

    for item in eth:
        print("{} : {}".format(item.name, item.oper))
