#!/usr/bin/env python

import numpy
import scipy

def inverter_de(x,t,h,i_out=10,v_in=300,params):
    """Calculate the differential equation for inverter hardware.

    This function calculates the differential equation of the inverter system
    at a given time and conditions with parameters supplied by dictionary.

    Inputs:
    x is the current system state in SI units arranged as an array
    [v_bus v_a v_b v_c i_a i_b i_c i_in]

    t is the current time in seconds

    h is the binary state of the three switching poles.  It is a vector with 
    the format is [h_a h_b h_c].

    i_out is the output current.  If this is a vector it is the current at
    each pole in amps as [i_a i_b i_c].  If this is a scalar it is the value
    of a star connected resistance.

    v_in is the system input voltage in volts.

    params is a dictionary of parameters defined as below.  All in natural SI
    units.

    r_s     : low side sensing resistance for each switch.
    r_in    : input resistance.
    l_in    : input inductance.
    c_bus   : DC-link capacitance
    v_swp   : switch constant on voltage with forward current
    v_swn   : switch constant on voltage with reverse current
    r_swp   : switch on-state resistance with forward current
    r_swn   : switch on-state resistance with reverse current
    l_f     : per-line filter inductance
    r_fs    : per-line filter inductor resistance
    c_f     : Y-filter capacitance
    """

    #First compute the output current if the resistor option is being used.
    i_out = array(i_out)
    if len(i_out) == 1:
        v_n = x[1:4].sum()/3
        i_out = (x[1:4] - v_n) / i_out
    

    v_bus_dot = (x[7] - h*x[4:7]) / params[c_bus]
    
