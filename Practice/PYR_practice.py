from neuron import h
from neuron.units import mV, ms
import sys, math
from matplotlib import pyplot

# In the paper the structure of the pyramidal neuron is considered as 
# BDEND === Soma === Aden1 === Aden2 === Aden3
# Therefore, based on the morphology file, we can represent the structure as 
# dend[4-8] == soma === dend1 === dend2 === dend3

# Load the standard run file below 


# This is a cell class that constructs a pyramidal cell with real morphology
class PYR:
    def __init__(self):
        # Open and executing the file generating geometry

        self.discretize()
        self.insert_general_mechanism()
        self.insert_dend1_mechanism()
        self.insert_dend2_mechanism()
        self.insert_dend3_mechanism()
        self.insert_dendf_mechanism()

    def discretize(self):
        """
        Discretize based on dLambda rule
        """
        
    
    def insert_general_mechanism(self):
        '''
        Mechanism used by all sections.

        Membrane mechanisms inserted in all sections are 'pas', 'nacurrent', 'kacurrent',
        'kdrcurrent', 'hcurrent'.

        All section parameters are specified at the center of each section.

        Parameters specification: axial resistivity 200 ohm-cm, g_pas = 0.0000357, 
        e_pas = -70. 
        '''
        

    def insert_dend1_mechanism(self):
        '''
        Dend 1 parameters

        Parameters specification: ki_nacurrent = 0.5, g_kacurrent = 0.072, v50_hcurrent = -82,
        g_hcurrent = 0.0002.
        '''
        

    def insert_dend2_mechanism(self):
        '''
        Dend 2 parameters

        Parameters specification: ki_nacurrent = 0.5, g_kacurrent = 0, gd_kacurrent = 0.120,
        v50_hcurrent = -90, g_hcurrent = 0.0004.
        '''
        

    def insert_dend3_mechanism(self):
        '''
        Dend 3 parameters

        Parameters specification: cm = 2, g_pas = 0.0000714,
        ki_nacurrent = 0.5, g_kacurrent = 0, gd_kacurrent = 0.2,
        v50_hcurrent = -90, g_hcurrent = 0.0007.
        '''


    def insert_dendf_mechanism(self):
        '''
        Rest of dend parameters (Remaining section parameters)

        Parameters specification: ki_nacurrent = 1
        '''


                
# Test the creation of the cell class. In this case, create a instance of pyramidal cell

# Plot the neuron using matplotlib NOT the NEURON's gui and show the plot

# Now, comment the plotting code above, and plot the created cell using NEURON gui and show it.

# Ensure the closure of the program running, press enter to terminate the run. 
