# custom table을 이용해서 user, class 가져오기

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

myYAML = """
---
UserTable:
    get: system/login/user
    view: UserView
UserView:
    fields:
        username: name
        userclass: class
"""

globals().update(FactoryLoader().load(yaml.load(myYAML, Loader=yaml.FullLoader)))

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    user = UserTable(dev)
    user.get()

    #print(user.keys())
    #print(user.values())

    for account in user:
        print("Username is {}\nUser Class is{}". format(account.username, account.userclass))
