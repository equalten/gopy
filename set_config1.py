# config를 서버에서 loading 하고 active config와 candidate config간 비료를 출력(pdiff())하고, commit

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per').open()

with Config(dev, mode='exclusive') as cu:
    cu.load(path='test1.conf', merge=True)
    cu.pdiff()
    #cu.commit()

    # rollback 2 config와 비교
    diff = cu.diff(rb_id=2)
    print(diff)

dev.close()
