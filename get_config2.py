# text 형태로 config 가져오기
# error에 대해서는 exception으로 핸들링

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from lxml import etree

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per')

try:
    dev.open()
#    with Config(dev, mode='ephemeral') as cu:
    with Config(dev) as cu:
        data = dev.rpc.get_config(option={'format':'text'})
        print(etree.tostring(data, encoding='unicode', pretty_print=True))
    dev.close()

except ConnectError as err:
    print("Cannot connect to device: {0}".format(err))
except Exception as err:
    print(err)