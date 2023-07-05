from netpyne import specs

# Simulation options
cfg = specs.SimConfig()        # object of class SimConfig to store simulation configuration
cfg.duration = 0.01*1e3           # Duration of the simulation, in ms
cfg.dt = 0.1                # Internal integration timestep to use
cfg.verbose = False            # Show detailed messages
# cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStep = 1             # Step size in ms to save data (eg. V traces, LFP, etc)

#------------------- Change neuron type here------------------------
# cfg.filename = 'PYR'  # Set file output name
# cfg.filename = 'SST'  # Set file output name
# cfg.filename = 'VIP'  # Set file output name
cfg.filename = 'PV'  # Set file output name
#-------------------------------------------------------------------

cfg.hParams['celsius'] = 37 

# cfg.recordLFP = [[x,y,z] for x in [146, 933] for y in [33,1136] for z in [5,138]]
# cfg.recordLFP = [[a,b,c] for a in [3,552]   for b in [66,1162] for c in [1,128]]
                #  [m,n,h] for m in [147,409] for n in [741,911] for h in [2,120],
                #  [e,f,g] for e in [187,950] for f in [141,1077] for g in [5,130]
                # ]
cfg.recordLFP = [[0,0,0],
                #  [100,100,100],
                #  [146,33,1],        #0
                #  [933,1136,1],      #1
                #  [3,66,1],          #2
                #  [552,1162,1],      #3
                #  [147,741,1],       #4
                #  [409,911,1],       #5
                 [187,141,1],       #6
                 [950,1077,1]]      #7

#------------------- Change neuron type here------------------------
# cfg.analysis['plotTraces'] = {'include': [('VIP',0)],
#                               #--------------------------------------
#                               'oneFigPer':'cell', 
#                               'overlay': False, 
#                               'figSize': (5,6),
#                               'saveFig': True}      # Plot recorded traces for this list of cells
cfg.analysis['plotLFP'] = {
                           'includeAxon': True, 
                           'plots': ['timeSeries',  'locations'], 
                           'plots': ['locations'], 
                           'figSize': (7.5,13.5), 
                           'saveFig': True,
                           'logx': True,
                            'logy': True,
                            }

#simConfig.analysis['getCSD'] = {'timeRange': [10,45],'spacing_um': 150, 'vaknin': True}
#simConfig.analysis['plotCSD'] = {'timeRange': [10,45]}
#sim.analysis.getCSD(...args...)
#simConfig.analysis['plotCSD'] = {}
