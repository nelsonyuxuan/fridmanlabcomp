#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:48:06 2021

@author: adam
"""
# from neuron import h
# h.nrnmpi_init()

# Last step, sum up all parameters from the network and the simulation parameters

from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='t42_cfg.py', 
                                           netParamsDefault='t42_netParams.py')

# Try to implement the plotRaster here to see if the time-range (x-axis) would change with time duration changes
simConfig.analysis['plotRaster'] = {'include': ['artif_pyr', 'PYR_pop', 'PVBC_pop', 'OLM_pop'],
                                    'marker': 'o',
                                    'saveFig': True, 
                                    'showFig': False, 
                                    'markerSize': 6}

# simConfig.duration = 1e+3
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

sim.pc.done()
#import sys
#sys.exit()
# h.quit()
