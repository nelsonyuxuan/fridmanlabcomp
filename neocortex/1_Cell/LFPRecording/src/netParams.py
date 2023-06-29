from netpyne import specs

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

netParams.sizeX = 100 # x-dimension (horizontal length) size in um
netParams.sizeY = 350 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 100 # z-dimension (horizontal length) size in um

                     
## Cell property rules
# netParams.loadCellParamsRule(label='Erule', fileName='cells/PT5B_full_cellParams.json')
# netParams.cellParams['Erule' ]['conds'] = {'cellType': ['E']}


# PYR cell loading
cellRule = netParams.importCellParams(
        label='PYR',
        conds={'cellType': 'PYR'},
        fileName='PYR_netpyne.py',
        cellName='PYR_netpyne',
        importSynMechs=False)

# SST cell loading
cellRule = netParams.importCellParams(
        label='SST',
        conds={'cellType': 'SST'},
        fileName='SST_netpyne.py',
        cellName='SST_netpyne',
        importSynMechs=False)

# VIP cell loading
cellRule = netParams.importCellParams(
        label='VIP',
        conds={'cellType': 'VIP'},
        fileName='VIP_netpyne.py',
        cellName='VIP_netpyne',
        importSynMechs=False)

# PV cell loading
cellRule = netParams.importCellParams(
        label='PV',
        conds={'cellType': 'PV'},
        fileName='PV_netpyne.py',
        cellName='PV_netpyne',
        importSynMechs=False)

# netParams.cellParams['Erule']['conds'] = {'cellType': ['E']}

## Population parameters
#------------------------ Change neuron type here------------------------
# netParams.popParams['E'] = {'cellType': 'PYR', 'numCells': 1}
# netParams.popParams['E'] = {'cellType': 'SST', 'numCells': 1}
netParams.popParams['E'] = {'cellType': 'VIP', 'numCells': 1}
# netParams.popParams['E'] = {'cellType': 'PV', 'numCells': 1}


## Synaptic mechanism parameters
# netParams.synMechParams['NMDA'] = {'mod': 'Exp2Syn', 'tau1': 2, 'tau2': 65, 'e': 0}  # excitatory synaptic mechanism, NMDA
# netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.3, 'tau2': 3, 'e': 0}  # excitatory synaptic mechanism, AMPA
# netParams.synMechParams['GABA'] = {'mod': 'Exp2Syn', 'tau1': 1, 'tau2': 10, 'e': -80}  # inbitary synaptic mechanism, GABA
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 
                                  'tau1': 0.8, 
                                  'tau2': 5.3, 
                                  'e': 0}  # NMDA synaptic mechanism

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 50, 'noise': 0.0, 'number': 1}
#------------------------ Change neuron type here------------------------
# netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 
#                                           'conds': {'cellType': ['PYR']}, 
#                                           'weight': 20.0, 
#                                           'sec': 'soma', 
#                                           'delay': 15, 
#                                           'synMech': 'exc'}
# netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 
#                                           'conds': {'cellType': ['SST']}, 
#                                           'weight': 20.0, 
#                                           'sec': 'soma', 
#                                           'delay': 15, 
#                                           'synMech': 'exc'}
netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 
                                          'conds': {'cellType': ['VIP']}, 
                                          'weight': 20.0, 
                                          'sec': 'soma', 
                                          'delay': 15, 
                                          'synMech': 'exc'}
# netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 
#                                           'conds': {'cellType': ['PV']}, 
#                                           'weight': 20.0, 
#                                           'sec': 'soma', 
#                                           'delay': 15, 
#                                           'synMech': 'exc'}
