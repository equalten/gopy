from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
from jnpr.junos.command.pfe_ddos_policer import DdosPolicerStatsTable
from pprint import pprint
import yaml
import json

json_table = """
---
DdosPolicerStatsTable:
  command: show ddos policer stats {{ protocol }} 
  args:
    protocol: ospf
  target: Null
  title: "DDOS Policer Statistics:"
  key: location
  view: DdosPolicerStatsView
"""

with Device(host='172.27.14.222', user='eknow', passwd='test1234') as dev:
    globals().update(FactoryLoader().load(yaml.load(json_table, Loader=yaml.FullLoader)))
    stats = DdosPolicerStatsTable(dev)
    stats.get(target='fpc0', args={ 'protocol' : 'bgp' })
    pprint (json.load(stats.to_json()))