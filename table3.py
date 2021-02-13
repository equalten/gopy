# external custom table을 이용해서 user 정보 가져오기
# /myTables의 .yml, .py 이용

from jnpr.junos import Device
from myTables.ConfigTables import UserTable
from pprint import pprint

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    users = UserTable(dev)
    users.get()

    pprint(users.items())    

    for account in users:
        print("User name: {}\nUser class: P{}".format(account.username, account.userclass))