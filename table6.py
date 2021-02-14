### 미완성임
### show system statiscs icmp 를 table로 만들기

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

yaml_data = """
---
IcmpStatistics:
    rpc: get-statistics-information
    args: 
        icmp = True
    item: icmp
    view: IcmpStatView

IcmpStatView:
    fields:
        drops_due_to_rate_limit: drops-due-to-rate-limit
        calls_to_icmp_error: calls-to-icmp-error
"""

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    globals().update(FactoryLoader().load(yaml.load(yaml_data, Loader=yaml.FullLoader)))
#    globals().update(FactoryLoader().load(yaml.load(yaml_data)))

    icmp_stat = IcmpStatistics(dev).get()
#    icmp_stat.get()
    print(icmp_stat.values())
    print(drops_due_to_rate_limit)
