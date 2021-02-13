from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

yaml_data = """
---
IcmpStatistics:
    rpc:get-statistics-information
    view:IcmpStatView
IcmpStatView:
    fields:
        drops_due_to_rate_limit: { drops-due-to-rate-limit : int }
        calls_to_icmp_error: { calls-to-icmp-error : int }
"""

globals().update(FactoryLoader().load(yaml.load(yaml_data, Loader=yaml.FullLoader)))

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    icmp = IcmpStatistics(dev).get('icmp')
    print(icmp.items())
