from netpyne import specs

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

netParams.sizeX = 500 # x-dimension (horizontal length) size in um
netParams.sizeY = 950 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 500 # z-dimension (horizontal length) size in um

## Population parameters
netParams.popParams['E'] = {'cellType': 'PYR', 
                            'numCells': 1, }
                        #     'yRange': [700,800]}

## Cell property rules
# netParams.loadCellParamsRule(label='Erule', fileName='cells/PT5B_full_cellParams.json')
# netParams.cellParams['Erule']['conds'] = {'cellType': ['E']}

# PYR cell loading
cellRule = netParams.importCellParams(
        label='PYR',
        conds={'cellType': 'PYR'},
        fileName='PYR_netpyne.py',
        cellName='PYR_netpyne',
        importSynMechs=False)

# SST cell loading
# cellRule = netParams.importCellParams(
#         label='SST',
#         conds={'cellType': 'SST'},
#         fileName='SST_netpyne.py',
#         cellName='SST_netpyne',
#         importSynMechs=False)

# VIP cell loading
# cellRule = netParams.importCellParams(
#         label='VIP',
#         conds={'cellType': 'VIP'},
#         fileName='VIP_netpyne.py',
#         cellName='VIP_netpyne',
#         importSynMechs=False)

# PV cell loading
# cellRule = netParams.importCellParams(
#         label='PV',
#         conds={'cellType': 'PV'},
#         fileName='PV_netpyne.py',
#         cellName='PV_netpyne',
#         importSynMechs=False)

## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 
                                  'tau1': 0.8, 
                                  'tau2': 5.3, 
                                  'e': 0}  # NMDA synaptic mechanism

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 
                                     'rate': 50, 
                                     'noise': 0.0, 
                                     'number': 1}
netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 
                                          'conds': {'cellType': ['PYR']}, 
                                          'weight': 20.0, 
                                          'sec': 'soma', 
                                          'delay': 15, 
                                          'synMech': 'exc'}
