from netpyne import specs

# Simulation options
cfg = specs.SimConfig()        # object of class SimConfig to store simulation configuration
cfg.duration = 0.05*1e3           # Duration of the simulation, in ms
cfg.dt = 0.1                # Internal integration timestep to use
cfg.verbose = False            # Show detailed messages
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStep = 1             # Step size in ms to save data (eg. V traces, LFP, etc)

#------------------- Change neuron type here------------------------
# cfg.filename = 'PYR'  # Set file output name
# cfg.filename = 'SST'  # Set file output name
cfg.filename = 'VIP'  # Set file output name
# cfg.filename = 'PV'  # Set file output name
#-------------------------------------------------------------------

cfg.hParams['celsius'] = 37 

cfg.recordLFP = [[x, y, 35] for y in range(742, 911, 50) for x in [150, 300]]

#------------------- Change neuron type here------------------------
# cfg.analysis['plotTraces'] = {'include': [('VIP',0)],
#                               #--------------------------------------
#                               'oneFigPer':'cell', 
#                               'overlay': False, 
#                               'figSize': (5,6),
#                               'saveFig': True}      # Plot recorded traces for this list of cells
cfg.analysis['plotLFP'] = {'includeAxon': False, 
                           'plots': ['timeSeries',  'locations'], 
                           'figSize': (7.5,13.5), 
                           'saveFig': True,
                            }

#simConfig.analysis['getCSD'] = {'timeRange': [10,45],'spacing_um': 150, 'vaknin': True}
#simConfig.analysis['plotCSD'] = {'timeRange': [10,45]}
#sim.analysis.getCSD(...args...)
#simConfig.analysis['plotCSD'] = {}
