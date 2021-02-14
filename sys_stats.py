from jnpr.junos import Device
from dictdiffer import diff
from lxml import etree
import jxmlease

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per', normalize=True)

dev.open()

rpc1 = dev.rpc.get_statistics_information()
rpc_xml1 = etree.tostring(rpc1, encoding='unicode', pretty_print=True)
xmlparser1 = jxmlease.Parser()
result1 = jxmlease.parse(rpc_xml1)
#print(result1)
#print(result1['statistics'].keys())
for table, proto, stat  in result1.items():
    print("\nStatistics: ", table)
    for protocols in proto:
        print('\nProtocols: ', protocols)
        for count in stat:
            print(count + ': ', protocols[key])

### working
#for table, proto in result1.items():
#    for protocols in proto:
#        print('\nProtocols: ', protocols)
###

#print(result1['statistics']['arp']['arp-iri-cnt'])

#rpc2 = dev.rpc.get_statistics_information()
#rpc_xml2 = etree.tostring(rpc2, encoding='unicode', pretty_print=True)
#xmlparser2 = jxmlease.Parser()
#result2=jxmlease.parse(rpc_xml2)
#
#ddiff = diff(result1, result2)
#diff_list = list(ddiff)
#print("====================")
#for item in diff_list:
##    pprint(item)
#    if "timeout" and "duplicate" in item[1]:
#        print("\033[44m" + item[1] + '\033[0m' + " : " + str(int(item[2][1]) - int(item[2][0])))
#    else:
#        print(item[1] + " : " + str(int(item[2][1]) - int(item[2][0])))