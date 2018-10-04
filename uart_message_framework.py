# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""

"""

__author__ = "Kyle Vitatus Lopin"

import binascii
import uart_communications as uart


class UARTComms(object):
    def __init__(self, uart_file: uart):
        commands = uart_file.commands  # type uart.AttributeDict
        print(commands)
        print(commands.STOP_SCAN)
        events = uart_file.events
        print(events)
        print(events.SCAN_PROGRESS_RESULT)
        print(type(events.SCAN_PROGRESS_RESULT))
        print(binascii.unhexlify("AAAA"))
        print(type(binascii.unhexlify("AAAA")))


if __name__ == "__main__":
    UARTComms(uart)
