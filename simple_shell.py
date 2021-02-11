from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell

dev = (host='172.27.14.72', user='jun', passwd='jun2per')

ss = StartShell(dev)
ss.open()
version = ss.run('cli -c "show version"')
print(version)
ss.close()
