import neuron
from neuron import h
from netpyne import specs, sim

# Create a cell parameter dictionary
cellParams = specs.CellParams()

# Load your the necessary HOC file
h.load_file('stdrun.hoc')
h.nrn_load_dll('nrnmech.dll')
h.load_file("import3d.hoc")
h.load_file('NeuronTemplate.hoc')
h.load_file('biophys_HL23SST.hoc')
h.load_file('PYRtemplate.hoc')

netParams = specs.NetParams()  # object of class NetParams to store the network parameters

# SUCCESSFUL import using the HOC template directly
# cellRule = netParams.importCellParams(
#         label='PYR',
#         conds={'cellType': 'PYR'},
#         fileName='PYRtemplate.hoc',
#         cellName='PYRtemplate',
#         importSynMechs=False)

#==========================LOAD CELL PARAMETERS==============================================
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
#========================================================================

#==========================POPULATION PARAMETERS==============================================
netParams.popParams['pre'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['sst'] = {'cellType': 'SST', 'numCells': 1}
netParams.popParams['post'] = {'cellType': 'PYR', 'numCells': 1}
#========================================================================

# # Set up simulation configuration
# simConfig = specs.SimConfig()  
# simConfig.duration = 1.0*1e3  # Duration of the simulation, in ms
# simConfig.dt = 0.025  # Internal integration timestep to use
# simConfig.verbose = False  # Show detailed messages

# # Create network and run simulation
# sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)


#==========================TEST CODE of LOADING BIOPHYSICAL PARAMETERS==============================================
# # Now you can access the biophysical parameters of your cells
# cell = sim.net.cells[0]  # Get the first cell
# cellProps = cell.__dict__  # Get the properties of the cell

# # Now print the properties
# for prop, value in cellProps.items():
#     print(f"{prop}: {value}")
#========================================================================