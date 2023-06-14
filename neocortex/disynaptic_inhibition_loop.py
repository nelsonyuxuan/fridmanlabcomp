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

#==========================LOAD CELL PARAMETERS (TEST COMPLETED)==============================================
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

#==========================POPULATION PARAMETERS (TEST COMPLETED)==============================================
netParams.popParams['pre'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['sst'] = {'cellType': 'SST', 'numCells': 1}
netParams.popParams['post'] = {'cellType': 'PYR', 'numCells': 1}
#========================================================================

#==========================SYNAPTIC PARAMETERS (TEST COMPLETED)==============================================
# Assume that the synaptic mechanisms defined by Exp2Syn is AMPA, which mainly contributes to the generation of EPSPs
netParams.synMechParams['excite_pyr_pre'] = {'mod': 'Exp2Syn', 'tau1': 0.3, 'tau2': 3, 'e': 0}  # excitatory synaptic mechanism
netParams.synMechParams['inhibit_sst_pre'] = {'mod': 'Exp2Syn', 'tau1': 1, 'tau2': 10, 'e': -80}  # inbitary synaptic mechanism
#========================================================================


#==========================STIMULATION PARAMETERS (TEST COMPLETED)==============================================
# Insert a current clamp to generate initial spike in the PYR cell.
netParams.stimSourceParams['CurrentClamp'] = {
    'type': 'IClamp',
    'amp': 1,  # amplitude of current, in nA
    'dur': 600,  # duration of current, in ms
    'delay': 50  # delay before current onset, in ms
}

netParams.stimTargetParams['IClamp->PYR'] = {
    'source': 'CurrentClamp',
    'conds': {'pop': 'pre'},
    'sec': 'soma_0',
    'loc': 0.5  # location of the stimulation
}
#========================================================================


#==========================CONNECTION PARAMETERS==============================================
# Excitatary synapses (TEST COMPLETED)
netParams.connParams['PYR->SST'] = {
    'preConds': {'pop': 'pre'},
    'postConds': {'pop': 'sst'},
    'weight': 0.01,  # Not really sure about the weight parameter values used for the parameters, waiting for adjustment. It seems like increasing the weight value will decrease the amplitude of the EPSPs
    'delay': 10, # Millisecond delay between when the pre-synaptic neuron fires and when that signal affects the post-synaptic neuron  
    'synMech': 'excite_pyr_pre',
    'sec': 'dend', # section of the postsynaptic cell to connect to 
    'synsPerConn': 25  
}

# Inhibitory synapses (TEST COMPLETED)
netParams.connParams['SST->PYR'] = {
    'preConds': {'pop': 'sst'},
    'postConds': {'pop': 'post'},
    'weight': 0.01,  # Not really sure about the weight parameter values used for the parameters, waiting for adjustment
    'delay': 1, # Millisecond delay between when the pre-synaptic neuron fires and when that signal affects the post-synaptic neuron  
    'synMech': 'inhibit_sst_pre',
    'sec': 'apical', # sections of the postsynaptic cell to connect to 
    'synsPerConn': 25 
}
#========================================================================

#==========================STIMULATION PARAMETERS==============================================
# Set up simulation configuration
simConfig = specs.SimConfig()  
simConfig.duration = 1.0*1e3  # Duration of the simulation, in ms
simConfig.dt = 0.025  # Internal integration timestep to use
simConfig.verbose = False  # Show detailed messages

# Record traces
# simConfig.recordTraces = {
#     'V_soma_pyr_pre': {'sec': 'soma_0','var': 'v', 'conds': {'pop':'pre', 'cellList': [0]}},
#     'V_soma_sst': {'sec': 'soma_0', 'var': 'v', 'conds': {'pop':'sst', 'cellList': [0]}},
#     'V_soma_pyr_post': {'sec': 'soma_0', 'var': 'v', 'conds': {'pop':'post', 'cellList': [0]}}
# }

simConfig.recordTraces = {'V_soma':{'sec':'soma_0','loc':0.5,'var':'v'}}  # Dict with traces to record

# Result control
simConfig.filename = 'Disynaptic_Inhibition_LOOP_MODEL'  # Set data output location
# simConfig.saveFig = '/Users/nelsonwu/Library/CloudStorage/OneDrive-Personal/FridmanLab/Computational_Project/neocortex_ABAN/FigureAndData'  # Set plot output location (NOT WORKING)
simConfig.analysis['plotRaster'] = {'saveFig': True}                  # Plot a raster"F""
simConfig.analysis['plot2Dnet'] = {'saveFig': True}                   # plot 2D cell positions and connections
simConfig.analysis['plotTraces'] = {'include': [('pre', 0), ('sst', 0), ('post', 0)], 'saveFig': True}  # Plot recorded traces for this list of cells

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)
#========================================================================


# #==========================TEST CODE of LOADING BIOPHYSICAL PARAMETERS==============================================
# # # Now you can access the biophysical parameters of your cells
# # cell = sim.net.cells[0]  # Get the first cell
# # cellProps = cell.__dict__  # Get the properties of the cell

# # # Now print the properties
# # for prop, value in cellProps.items():
# #     print(f"{prop}: {value}")

# # Check if the section 'somatic' exists for each cell in your desired population.
# for cell in sim.net.cells:
#     if cell.tags['pop'] in ['pre', 'post', 'sst']:  # Replace with your population names
#         if 'soma' in cell.secs:
#             print(f"Cell {cell.gid} in population {cell.tags['pop']} has a 'soma' section.")
#         else:
#             print(f"Cell {cell.gid} in population {cell.tags['pop']} does not have a 'soma' section.")

# Then print section names for each cell of desired population
# for cell in sim.net.cells:
#     if cell.tags['pop'] in ['pre', 'post', 'sst']:  # Replace with your population names
#         print(f"Cell {cell.gid} in population {cell.tags['pop']} has the following sections:")
#         for sec in cell.secs:
#             print(f"    {sec}")

# print(sim.net.cells)

# for cell in sim.net.cells:
#     print('Cell GID:', cell.gid)  # print cell global identifier
#     print('Cell Tags:', cell.tags)  # print cell properties
#     print('Cell sections:', cell.secs.keys())  # print section names of the cell
#     print('-------------------')

# #========================================================================