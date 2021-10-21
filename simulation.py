from NWNetworkSimulator import *

import logging

###############################################################################
# NETWORK SETUP

connections = NetworkUtils.generate(default)
graph = NetworkUtils.get_graph(connections)

###############################################################################
# ELECTRICAL STIMULATION

logging.info('Electrical stimulation of the network')

timesteps = 90          # simulation duration
pulse_duration = 10     # duration of a stimulation pulse (in timesteps)
reads = 80              # reads at output
pulse_count = 1         # number of stimulation pulses
delta_t = 0.05          # virtual time delta

v = 10                  # pulse amplitude of stimulation

# stimulate for 10 timesteps and then rest
Vins = [0.01] + [v] * pulse_duration * pulse_count + [0.01] * reads

# growth of the conductive path
logging.debug('Growth of the conductive path')

# pristine state - create stimulator that initialize the state (todo ?)
stimulator = NetworkStimulator(graph, device=default)

# growth over time
for i in range(0, int(timesteps)):
    stimulator.stimulate(default.sourcenode, default.groundnode, Vins[i])

information_centrality(stimulator.H)

###############################################################################
# PLOTTING

#inspect(graph)
#plot.plot(lambda: plot.adj_matrix(connections))
