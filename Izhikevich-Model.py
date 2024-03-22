import numpy as np
import matplotlib.pyplot as plt

x  = 4.1
y  = 108

# titles = ['Regular Spiking', 'Chattering', 'Fast Spiking', 'Intrinsically Bursting','Low-Threshold Spiking']
# a  = [0.02, 0.02, 0.1, 0.02, 0.02]
# b  = [0.2 , 0.2 , 0.2, 0.2 ,0.25]
# c  = [-65 , -50 , -65, -55 , -65]
# d  = [8   , 2   , 2  , 5   , 2]


# v0 = -70    # Resting potential        [mV]
# T = 200     # Simulation time          [mSec]
# dt = 0.25   # Simulation time interval [mSec]

# #VALUES FOR THALAMO -87mV
# titles = ['Thalamo-Cortical; -63 mV', 'Thalamo-Cortical; -87 mV']
# a  = [0.02, 0.02]
# b  = [0.25, 0.25]
# c  = [-65 , -65]
# d  = [0.05, 0.05]

# v0 = -87    # Resting potential        [mV]
# T = 200     # Simulation time          [mSec]
# dt = 0.25   # Simulation time interval [mSec]


#VALUES FOR RESONATOR 
titles = ['Resonator']

a = [0.1]
b = [-0.1]
c = [-65]
d = [8]

v0 = -70    # Resting potential        [mV]
T = 200     # Simulation time          [mSec]
dt = 0.25   # Simulation time interval [mSec]

time = np.arange(0, T + dt, dt)  # Time array

stim = np.zeros(len(time))
for i,t in enumerate(stim):
    if i > 20:
        stim[i] = 1
        stim[400:410] = 8
    # else:
    #     stim[i] = -1   #Negative stim for 20ms (THALAMO-CORTICAL -87)

trace = np.zeros((2,len(time))) # Tracing du and dv

for exp in range(len(a)):
    v  = v0
    u  = b[exp]*v
    spikes = []
    for i, j in enumerate(stim):
        v += dt * (0.04*v**2 + x*v + y - u + stim[i]) 
        u += dt * a[exp]*(b[exp]*v-u)
        if v > 30:
            trace[0,i] = 30
            v = c[exp] 
            u += d[exp]
        else:
            trace[0,i] = v 
            trace[1,i] = u

    plt.figure(figsize=(10,5))
    plt.title('Izhikevich Model: {}'.format(titles[exp]), fontsize=15) 
    plt.ylabel('Membrane Potential (mV)', fontsize=15) 
    plt.xlabel('Time (msec)', fontsize=15)
    plt.plot(time, trace[0], linewidth=2, label = 'Vm')
    plt.plot(time, trace[1], linewidth=2, label = 'Recovery', color='green')
    plt.plot(time, stim + v0, label = 'Stimuli (Scaled)', color='sandybrown', linewidth=2)
    plt.legend(loc=1)
    plt.show()