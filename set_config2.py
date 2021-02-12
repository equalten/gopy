from jnpr.junos import Device
from myTables.ConfigTables import UserConfigTable

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per').open()

with UserConfigTable(dev, mode='private') as cu:
    cu.user = 'user1'
    cu.class_name = 'read-only'
    cu.append()

    cu.load(merge=True)
    cu.pdiff()
    #cu.commit()

dev.close()
