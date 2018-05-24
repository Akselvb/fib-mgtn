# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:49:07 2018

@author: joseb
"""

import numpy as np

#%%
########################################################
######## X-MAC: Trade_off Energy with Delay using GT
########################################################
# Radio subsystem varaible definition

P     = 32.            # Payload [byte]
R     = 31.25          # CC2420 Radio Rate [kbyte/s]
D     = 8              # number of levels
C     = 5              # neighbors size (connectivity)
N     = C*D**2          # number of nodes
Lmax  = 5000.          # Maximal allowed Delay (ms)
Emax  = 1.            # MAximal Energy Budjet (J)

L_pbl = 4.             # preamble length [byte]
L_hdr = 9. + L_pbl     # header length [byte]
L_ack = 9. + L_pbl     # ACK length [byte]
L_ps  = 5. + L_pbl     # preamble strobe length [byte]

Tal  = 0.95            # ack listen period [ms]
Thdr = L_hdr/R         # header transmission duration [ms]
Tack = L_ack/R         # ACK transmission duration [ms]
Tps  = L_ps/R          # preamble strobe transmission duration [ms]
Tcw  = 15*0.62         # Contention window size [ms]
Tcs  = 2.60            # Time [ms] to turn the radio into TX and probe the channel (carrier sense)
Tdata = Thdr + P/R + Tack # data packet transmission duration [ms]

#%%%%%%
### Some parameters to play

### Sampling frequency
Fs   = 1.0/(60*30*1000)    # e.g. Min traffic rate 1 pkt/half_hour = 1/(60*30*1000) pk/ms

# Sleep period: Parameter Bounds
Tw_max  = 500.       # Maximum Duration of Tw in ms
Tw_min  = 100.       # Minimum Duration of Tw in ms

#%%
# Traffic calculation as a function of number of levels
Fout_d = np.zeros((D+1,1))
Fin_d  = np.zeros((D+1,1))
F_B_d  = np.zeros((D+1,1))
Fin_d[0]=D**2*C
for i in range(1,D):
    Fout_d[i] = (D**2 - i**2 + 2*i-1)/(2*i-1)
    Fin_d[i] =  (D**2 - i**2)/(2*i-1)    
    F_B_d[i] =  Fout_d[i]*(C - (2*i+1)/(2*i-1))

#Fin_d(0)  = F_s*D^2*C

Fout_d[D] = 1.0
Fin_d[D]  = 0.0
F_B_d[D]  = C*Fout_d[D]


#%%
# Network Topology, node(i) indicates at which level is each node, 
# e.g. nodes 0 to 7 are at level d=1, nodes 8 to 15 at level 2, ...  
# node[j] stores de ring at which node j belongs.

print '\n number of nodes = ',N
print '\n number of rings = ',D 
print '\n Average number of neigbors per node = ',C
index = 0
node=np.zeros((N,1),dtype=int)
print '\n Number of neighbors per ring is Nd = (2d-1)*C'
for i in range(1,D+1):
    print '      Ring d =',i, ' has Nd = ',(2*i-1)*C,' nodes'
    for j in range(index,index + (2*i-1)*C):
        node[j]=i
#        print 'node number = ',j,'ring = ',node[j]
    index = index + (2*i-1)*C

