#!/usr/bin/env python3

# eteint toutes les led

import tm1637

def demarrage():
    tm = tm1637.TM1637(clk=5, dio=4)

    # all LEDS off
    tm.write([0, 0, 0, 0])


