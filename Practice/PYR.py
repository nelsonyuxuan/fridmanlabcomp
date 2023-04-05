from neuron import h
from neuron.units import mV, ms
import sys, math
from matplotlib import pyplot

h.load_file('stdrun.hoc')

# In the paper the structure of the pyramidal neuron is considered as 
# BDEND === Soma === Aden1 === Aden2 === Aden3
# Therefore, based on the morphology file, we can represent the structure as 
# dend[4-8] == soma === dend1 === dend2 === dend3

class PYR:
    def __init__(self):
        # Open and executing the file generating geometry
        h.xopen("ca3a.geo")

        self.discretize()
        self.insert_general_mechanism()
        self.insert_dend1_mechanism()
        self.insert_dend2_mechanism()
        self.insert_dend3_mechanism()
        self.insert_dendf_mechanism()

    def discretize(self):
        """
        dlamb rule : see NEURON :  a tool for neuroscientist, 2001
        """
        freq, d_lam = 100, 0.1
        for sec in h.allsec():
            sec.nseg = math.ceil( (sec.L/(d_lam * h.lambda_f(freq) ))/2.0 )*4 +1 
    
    def insert_general_mechanism(self):
        '''
        Mechanism used by all sections 
        '''
        
        for sec in h.allsec():

            sec.Ra = 200

            sec.insert('pas')
            sec.insert('nacurrent')
            sec.insert('kacurrent')
            sec.insert('kdrcurrent')
            sec.insert('hcurrent')
            sec(0.5).g_pas = 0.0000357
            sec(0.5).e_pas = -70
            
            # for seg in sec.allseg():
            
                # Pas
                # seg.e_pas = -65
                # seg.g_pas = 1/600000

    def insert_dend1_mechanism(self):
        '''
        Dend 1 parameters
        '''
        
        for sec in h.dend1:
            sec(0.5).ki_nacurrent = 0.5
            sec(0.5).g_kacurrent = 0.072
            sec(0.5).v50_hcurrent = -82
            sec(0.5).g_hcurrent = 0.0002

    def insert_dend2_mechanism(self):
        '''
        Dend 2 parameters
        '''
        
        for sec in h.dend2:
            sec(0.5).ki_nacurrent = 0.5
            sec(0.5).g_kacurrent = 0
            sec(0.5).gd_kacurrent = 0.120
            sec(0.5).v50_hcurrent = -90
            sec(0.5).g_hcurrent = 0.0004

    def insert_dend3_mechanism(self):
        '''
        Dend 3 parameters
        '''
        
        for sec in h.dend3:
            sec(0.5).cm = 2
            sec(0.5).g_pas = 0.0000714
            sec(0.5).ki_nacurrent = 0.5
            sec(0.5).g_kacurrent = 0
            sec(0.5).gd_kacurrent = 0.2
            sec(0.5).v50_hcurrent = -90
            sec(0.5).g_hcurrent = 0.0007

    def insert_dendf_mechanism(self):
        '''
        Rest dend parameters
        '''

        dend_loc = [ sec for sec in h.allsec() if sec not in h.dend1 and sec not in h.dend2 and sec not in h.dend3]
        
        for sec in dend_loc:

            sec(0.5).ki_nacurrent = 1

                
# Test the creation of the cell class
c = PYR()

ps = h.PlotShape(False)  # False tells h.PlotShape not to use NEURON's gui
ps.plot(pyplot)
pyplot.show()

# input('') # Ensure the closure of the program running, press enter to terminate the run. 


# ps = h.PlotShape(True)
# ps.variable("v")
# ps.show(0)

input('') # Ensure the closure of the program running, press enter to terminate the run. 
