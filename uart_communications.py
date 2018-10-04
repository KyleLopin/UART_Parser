# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""

"""

__author__ = "Kyle Vitatus Lopin"


class AttributeDict(dict):
    def __init__(self, **kwarg):
        super().__init__(**kwarg)

    def __getattr__(self, attr):
        if isinstance(attr, str):
            return self[attr]
        elif isinstance(attr, bytes):
            return

    def __setattr__(self, key, value):
        self[key] = value


# commands are sent to the MCU
command_structure = "[ cmd_header | address | command | length | data ]"
# events received from MCU
event_structure = "[ evt_header | len | event | req_cmd | data ]"

address = '59'

cmd_header = '43'
cmd_footer = '0000'

commands = AttributeDict(
    Resolve_and_Set_Peer_Device_BD_Address="A1FE",
    INIT_BLE_STACK="07FC",
    START_SCAN="93FE",
    STOP_SCAN="94FE",
)

evt_header = "BDA7"

events = AttributeDict(
    SCAN_PROGRESS_RESULT="8A06",
    COMMAND_STATUS="7E04",
)
