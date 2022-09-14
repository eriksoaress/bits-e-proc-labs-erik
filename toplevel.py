#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from myhdl import *

from comb.comb_modules import *
from ula.ula_modules import *
from seq.seq_modules import *


@block
def toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, CLOCK_50, RESET_N):
    sw_s = [SW(i) for i in range(10)]
    key_s = [KEY(i) for i in range(10)]
    ledr_s = [Signal(bool(0)) for i in range(10)]

    # ---------------------------------------- #
    # comb
    # ---------------------------------------- #
    # ic1 = exe4(ledr_s, SW)
    # ic2 = exe5(ledr_s, SW)
    # ic2 = sw2hex(HEX0, SW)
    # ic3 = bin2hex(HEX1, SW)

    # ---------------------------------------- #
    # ula
    # ---------------------------------------- #
    ic1 = adder(sw_s[0:4], sw_s[6:10], ledr_s[0:4], ledr_s[9])

    ledr_unsigned = ConcatSignal(*reversed(ledr_s))
    ic2 = bin2hex(HEX0, ledr_unsigned)

    # ---------------------------------------- #
    # seq
    # ---------------------------------------- #
    # ic0 = dff(ledr_s[0], sw_s[0], key_s[0], RESET_N)
    # ic1 = blinkLed(ledr_s[0], 100, CLOCK_50, RESET_N)
    # ic2 = blinkLed(ledr_s[1], 50, CLOCK_50, RESET_N)
    # ic3 = blinkLed(ledr_s[2], 1000, CLOCK_50, RESET_N)
    # ic1 = stepMotor(LEDR, sw_s[0], sw_s[1], CLOCK_50, RESET_N)

    # ---------------------------------------- #
    @always_comb
    def comb():
        for i in range(len(ledr_s)):
            LEDR[i].next = ledr_s[i]

    #        for i in range(len(hex0_s)):
    #            HEX0[i].next = hex0_s[i]
    #            HEX1[i].next = hex1_s[i]
    #            HEX2[i].next = hex2_s[i]
    #            HEX3[i].next = hex3_s[i]
    #            HEX4[i].next = hex4_s[i]
    #            HEX5[i].next = hex5_s[i]

    return instances()


LEDR = Signal(intbv(0)[10:])
SW = Signal(intbv(0)[10:])
KEY = Signal(intbv(0)[4:])
HEX0 = Signal(intbv(1)[7:])
HEX1 = Signal(intbv(1)[7:])
HEX2 = Signal(intbv(1)[7:])
HEX3 = Signal(intbv(1)[7:])
HEX4 = Signal(intbv(1)[7:])
HEX5 = Signal(intbv(1)[7:])
CLOCK_50 = Signal(bool())
RESET_N = ResetSignal(0, active=0, isasync=True)

top = toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, CLOCK_50, RESET_N)
top.convert(hdl="VHDL")
