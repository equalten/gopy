from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    icmp = dev.rpc.get_statistics_information(icmp=True)

drops_due_to_rate_limit = icmp.find('.//drops-due-to-rate-limit').text
print(drops_due_to_rate_limit)
