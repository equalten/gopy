from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortErrorTable
from pprint import pprint

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    int_err = PhyPortErrorTable(dev).get()

    #pprint(int_err.keys())
    #pprint(int_err.values())
    #pprint(int_err.items())

    print("Interface    RX Errors   TX Errors")
    for interface in int_err:
    #    data = interface.values()
        rx_err = 0
        tx_err = 0
        data = interface.values()
        for i in range(4, 14):
            rx_err += data[i]
        for j in range(14, 23):
            tx_err += data[j]
        print("{}           {}          {}".format(interface, rx_err, tx_err))
    #    pprint(data[1])
    #    pprint(data[2])

    #    for err in int_err.values():
    #        pprint(err)

    #    print(interface)
    #    print(interface.rx_err_l3_incompletes)
    #   rx_err = interface.rx_err_input + interface.rx_err_drops + interface.rx_err_frame + interface.rx_err_runts + interface.rx_err_discards + interface.rx_err_l3-incompletes + interface.rx_err_l2-channel + interface.rx_err_l2-mismatch + interface.rx_err_fifo + interface.rx_err_resource
    #    tx_err = interface.tx_err_carrier-transitions + interface.tx_err_output + interface.tx_err_collisions + interface.tx_err_drops + interface.tx_err_aged + interface.tx_err_mtu + interface.tx_err_hs-crc + interface.tx_err_fifo + interface.tx_err_resource

    #    print("Interface: {}\n  Input Error: {}\n  Input Drops: {}".format(interface, interface.rx_err_input, interface.rx_err_drops))