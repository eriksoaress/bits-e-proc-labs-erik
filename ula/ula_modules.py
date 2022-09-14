#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a and b        

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    half1 = halfAdder(a,b, s[0], s[1])
    half2 = halfAdder(c, s[0], soma, s[2])
    @always_comb
    def comb():
        carry.next = s[1] | s[2]
        pass

    return instances()


@block
def adder2bits(x, y, soma, carry):
    carry0 = Signal(bool(0))
    carry1 = Signal(bool(0))
    full0 = fullAdder(x[0], y[0], carry0, soma[0], carry1)
    full1 = fullAdder(x[1], y[1], carry1, soma[1], carry)
    return instances()


@block
def adder(x, y, soma, carry):
    s = [Signal(bool(0)) for i in range(len(x))]
    fullList = [None for i in (range(len(x)-1))]
    for i in range(len(x)-1):
        fullList[i] = fullAdder(x[i], y[i], s[i], soma[i], s[i+1])
 
    @always_comb
    def comb():
        carry.next = s[len(x)-1]
        pass

    return instances()
