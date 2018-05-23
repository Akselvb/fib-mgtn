import numpy as np
import matplotlib.pyplot as plt


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
Tw_max  = 500       # Maximum Duration of Tw in ms
Tw_min  = 100       # Minimum Duration of Tw in ms

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

A1 = (Tcs+Tal)
A2 = ((Tps+Tal)/2.0 + Tcs + Tack + Tal + Tdata ) * Fout_d[1] + Fin_d[1] * (3.0/2.0 * (Tps+Tack+Tdata)) + F_B_d[1] * 3.0/4.0*Tps
A2 = A2[0]
A3 = 3.0/2.0*Tps*((Tps+Tal)/2+Tack+Tdata)*F_B_d[1]
A3 = A3[0]
A4 = Fout_d[1]/2.0
A4 = A4[0]

E=[]
L=[]

for Fs in [1.0/(60.0*30.0*1000.0), 2.0/(60.0*30.0*1000.0), 6.0/(60.0*30.0*1000.0), 9000000.0/(60.0*30.0*1000.0)]:
    j=0
    alpha1=A1+A3*Fs
    alpha2=A4*Fs
    alpha3=A2*Fs

    # print("A1")
    # print(A1)
    # print("A2")
    # print(A2)
    # print("A3")
    # print(A3)
    # print("A4")
    # print(A4)
    # print("alpha1")
    # print(alpha1)
    # print("alpha2")
    # print(alpha2)
    # print("alpha3")
    # print(alpha3)

    # Compute Betas

    beta1 = 0
    for i in range(D):
      beta1 += 1/2

    beta2 = 0
    for i in range(D):
      beta2 += (Tcw/2)+Tdata

    #
    # print('beta1')
    # print(beta1)
    # print('beta2')
    # print(beta2)

    Es = []
    Ls = []

    # Calculate E and L
    for Tw in range(int(Tw_min), int(Tw_max)):
        Es.append(((alpha1/Tw)+(alpha2*Tw)+alpha3))
        Ls.append(((beta1*Tw)+beta2))


    E.append(Es)
    L.append(Ls)

# Create the graphs
for i in range(len(E)):
    plt.plot(E[i])
    plt.savefig('Energy' + str(i) + '.png')
    plt.clf()

    plt.plot(L[i])
    plt.savefig('Delay' + str(i) + '.png')
    plt.clf()

    plt.plot(E[i], L[i])
    plt.savefig('Energy-delay' + str(i) + '.png')
    plt.clf()
