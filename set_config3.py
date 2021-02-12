# set을 이용한 config : Unstructed method

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per').open()

with Config(dev, mode='private') as cu:
    cu.load('set system services netconf traceoptions file test.log', format='set')
    cu.pdiff()
    #cu.commit()

dev.close()
