### pip install jxmlease 필요
### https://www.inetzero.com/pyez/

from jnpr.junos import Device
from deepdiff import DeepDiff
from dictdiffer import diff
from lxml import etree
from pprint import pprint
import jxmlease

dev = Device(host='172.27.14.72', user='jun', passwd='jun2per', normalize=True)

dev.open()

rpc1 = dev.rpc.get_statistics_information()
rpc_xml1 = etree.tostring(rpc1, encoding='unicode', pretty_print=True)
#print(rpc_xml)
xmlparser1 = jxmlease.Parser()
result1 = jxmlease.parse(rpc_xml1)
#print(result1)

rpc2 = dev.rpc.get_statistics_information()
rpc_xml2 = etree.tostring(rpc2, encoding='unicode', pretty_print=True)
xmlparser2 = jxmlease.Parser()
result2=jxmlease.parse(rpc_xml2)
#print(result2)

ddiff = diff(result1, result2)
diff_list = list(ddiff)
print("====================")
for item in diff_list:
#    pprint(item)
    if "timeout" and "duplicate" in item[1]:
        print("\033[44m" + item[1] + '\033[0m' + " : " + str(int(item[2][1]) - int(item[2][0])))
    else:
        print(item[1] + " : " + str(int(item[2][1]) - int(item[2][0])))


#ddiff = DeepDiff(result1, result2)
#pprint(ddiff)

#print(result)
#print("=================")

#for count1, count2 in result.items():
#    print(count2['calls-to-icmp-error'])
#print(result.items())
#calls_to_icmp_error1=result['statistics']['icmp']['calls-to-icmp-error']
#print(int(calls_to_icmp_error1)+1)
#for count in result['statistics']['icmp']:
#    print(count['calls-to-icmp-error'])
#    print(count)
