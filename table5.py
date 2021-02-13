from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

yaml_data = """
---
PhyPortTable:
  rpc: get-interface-information
  args:
    interface_name: '[efgx][et]-*'
  args_key: interface_name
  item: physical-interface
  view: PhyPortView

PhyPortView:
  fields:
    oper : oper-status
    admin : admin-status
    description: description
    mtu: { mtu : int }
    link_mode: link-mode
    speed: speed
    macaddr: current-physical-address
    flapped: interface-flapped

### ---------------------------------------------------------------------------
### get extensive information
### ---------------------------------------------------------------------------

PhyPortStatsTable:
  rpc: get-interface-information
  args:
    extensive: True
    interface_name: '[efgx][et]-*'
  args_key: interface_name
  item: physical-interface
  view: PhyPortStatsView

PhyPortStatsView:
  groups:
    ts: traffic-statistics
    rxerrs: input-error-list

  # fields that are part of groups are called
  # "fields_<group-name>"

  fields_ts:
    rx_bytes: { input-bytes: int }
    rx_packets: { input-packets: int }
    tx_bytes: { output-bytes: int }
    tx_packets: { output-packets: int }

  fields_rxerrs:
    rx_err_input: { input-errors: int }
    rx_err_drops: { input-drops: int }

PhyPortErrorTable:
  rpc: get-interface-information
  args:
    extensive: True
    interface_name: '[efgx][et]-*'
  args_key: interface_name
  item: physical-interface
  view: PhyPortErrorView

PhyPortErrorView:
  groups:
    ts: traffic-statistics
    rxerrs: input-error-list
    txerrs: output-error-list

  # fields that are part of groups are called
  # "fields_<group-name>"

  fields_ts:
    rx_bytes: { input-bytes: int }
    rx_packets: { input-packets: int }
    tx_bytes: { output-bytes: int }
    tx_packets: { output-packets: int }

  fields_rxerrs:
    rx_err_input: { input-errors: int }
    rx_err_drops: { input-drops: int }
    rx_err_frame: { framing-errors: int }
    rx_err_runts: { input-runts: int }
    rx_err_discards: { input-discards: int }
    rx_err_l3_incompletes: { input-l3-incompletes: int }
    rx_err_l2_channel: { input-l2-channel-errors: int }
    rx_err_l2_mismatch: { input-l2-mismatch-timeouts: int }
    rx_err_fifo: { input-fifo-errors: int }
    rx_err_resource: { input-resource-errors: int }

  fields_txerrs:
    tx_err_carrier_transitions: { carrier-transitions: int }
    tx_err_output: { output-errors: int }
    tx_err_collisions: { output-collisions: int }
    tx_err_drops: { output-drops: int }
    tx_err_aged: { aged-packets: int }
    tx_err_mtu: { mtu-errors: int }
    tx_err_hs_crc: { hs-link-crc-errors: int }
    tx_err_fifo: { output-fifo-errors: int }
    tx_err_resource: { output-resource-errors: int }
"""

globals().update(FactoryLoader().load(yaml.load(yaml_data, Loader=yaml.FullLoader)))

with Device(host='172.27.14.72', user='jun', passwd='jun2per') as dev:
    int_err = PhyPortErrorTable(dev).get()

    print("Interface    RX Errors    TX Errors")
    print("===================================")
    for interface in int_err:
        rx_err = interface.rx_err_input + interface.rx_err_drops + interface.rx_err_frame + interface.rx_err_runts + interface.rx_err_discards + interface.rx_err_l3_incompletes + interface.rx_err_l2_channel + interface.rx_err_l2_mismatch + interface.rx_err_fifo + interface.rx_err_resource
        tx_err = interface.tx_err_carrier_transitions + interface.tx_err_output + interface.tx_err_collisions + interface.tx_err_drops + interface.tx_err_aged + interface.tx_err_mtu + interface.tx_err_hs_crc + interface.tx_err_fifo + interface.tx_err_resource
        if rx_err==0 and tx_err==0:
            continue
        else:
            print("{}        {}          {}".format(interface.name, rx_err, tx_err))

