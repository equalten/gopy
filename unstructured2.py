from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import json

tv = """
---
Cmerror:
  command: show cmerror level
  key: Level
  view: CmerrorView

CmerrorView:
  columns:
    lev: Level
    cnt: Count
    occ: Occurred
    clr: Cleared
    thr: Threshold
    rli: R-Limit
    act: Action
"""

with Device(host='172.27.14.222', user='eknow', passwd='test1234') as dev:
    globals().update(FactoryLoader().load(yaml.load(tv, Loader=yaml.FullLoader)))
    rt=Cmerror(dev)
    rt.get(target='fpc0')
    print(json.dumps(json.loads(rt.to_json()), indent=4))
