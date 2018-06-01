import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from gpkit import Variable, Model
import math


########################################################
######## X-MAC: Trade_off Energy with Delay using GT   #
########################################################
# Radio subsystem varaible definition

P     = 32.            # Payload [byte]
R     = 31.25          # CC2420 Radio Rate [kbyte/s]
D     = 8              # number of levels
C     = 5              # neighbors size (connectivity)
N     = C*D**2         # number of nodes
Lmax  = 5000.          # Maximal allowed Delay (ms)
Emax  = 1.             # MAximal Energy Budjet (J)

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

Fout_d[D] = 1
Fin_d[D]  = 0
F_B_d[D]  = C*Fout_d[D]





###############
#   TASK 1    #
###############

print "\nCompute parameters alpha and beta."
A1 = (Tcs+Tal)
A2 = ( (Tps+Tal)/2.0 + Tcs + Tack + Tal + Tdata ) * Fout_d[1] + Fin_d[1] * (3.0/2.0 * (Tps+Tack+Tdata)) + F_B_d[1] * 3.0/4.0*Tps
A2 = A2[0]
A3 = (3.0/2.0)*Tps*((Tps+Tal)/2+Tack+Tdata)*F_B_d[1] # 3/2 will affect A3 and the following dependent variables.
A3 = A3[0]
A4 = Fout_d[1]/2.0
A4 = A4[0]

beta1 = 0
for i in range(D):
  beta1 += 1.0/2.0

beta2 = 0
for i in range(D):
    beta2 += (Tcw/2.0)+Tdata

print "\tDone.\n"

print "Calculate energy consumption and delay for different values."
E = []
L = []
for Fs in [1.0/(60*30*1000), 2.0/(60*30*1000), 6.0/(60*30*1000), 9000000.0/(60*30*1000)]:
    j = 0
    alpha1 = A1+A3*Fs
    alpha2 = A4*Fs
    alpha3 = A2*Fs

    Es = []
    Ls = []

    # print(A1)
    # print(A2)
    # print(A3)
    # print(A4)
    # print(alpha1)
    # print(alpha2)
    # print(alpha3)
    # print(beta1)
    # print(beta2)
    # print ""

    # Calculate E and L
    for Tw in range(int(Tw_min), int(Tw_max)):
        Es.append(((alpha1/Tw)+(alpha2*Tw)+alpha3))
        Ls.append(((beta1*Tw)+beta2))

    E.append(Es)
    L.append(Ls)

print "\tDone.\n"


print "Construct graphs according to different values."
for i in range(len(E)):
    plt.title("Energy consumption as a function of sleep time")
    plt.xlabel("Tw")
    plt.ylabel("E")
    plt.plot(E[i])
    plt.savefig('images/energy' + str(i) + '.png')
    plt.clf()

    plt.title("Delay as a function of sleep time")
    plt.xlabel("Tw")
    plt.ylabel("L")
    plt.plot(L[i])
    plt.savefig('images/delay' + str(i) + '.png')
    plt.clf()

    plt.title("Energy consumption as a function of delay")
    plt.xlabel("L")
    plt.ylabel("E")
    plt.plot(L[i], E[i])
    plt.savefig('images/energy-delay' + str(i) + '.png')
    plt.clf()

print "\tDone.\n"




#############
#   TASK 2  #
#############

# Fs = 1.0/(60*30*1000)
# alpha1 = A1+A3*Fs
# alpha2 = A4*Fs
# alpha3 = A2*Fs
#
# # Decision variables
# x = Variable("x")
# y = Variable("Fout_d", Fout_d[1])
# z = Variable("test", ((Tcs + Tal + x/2.0 + Tack + Tdata) * y * Fs * C))
#
# E = []
# L = []
#
# print "Optimization: Minimize energy consumption according to different values for maximum delay."
# for Lmax in range(1000, 5000, 10):
#     # Constraint
#     constraints = [Lmax >= beta1 * x + beta2, Tw_min <= x, Tw_max >= x, z <= 0.25]
#
#     # Objective (to minimize)
#     objective = alpha1/x + alpha2*x + alpha3
#
#     # Formulate the Model
#     m = Model(objective, constraints)
#
#     # Solve the Model
#     sol = m.debug(verbosity=0)#sol = m.solve(verbosity=0)
#
#     E.append(sol['cost'])
#     L.append(Lmax)
#
#
# print "Construct graph of optimization problem."
# plt.title("Minimization of energy constrained to different maximum delays.")
# plt.xlabel("L_max")
# plt.ylabel("E_min")
# plt.plot(L, E)
# plt.savefig('images/minimize_energy.png')
# plt.clf()
#
#
# print "Optimization: Minimize delay according to different values for energy budget"
# E = []
# L = []
# e_budget = 0.017
# while e_budget < 0.1:
#     e_budget += 0.0002
#
#     # Constraint
#     constraints = [e_budget >= alpha1/x + alpha2*x + alpha3, Tw_min <= x, Tw_max >= x, z <=0.25]
#
#     # Objective (to minimize)
#     objective = beta1*x + beta2
#
#     # Formulate the Model
#     l = Model(objective, constraints)
#
#     # Solve the Model
#     sol = l.debug(verbosity=0)
#
#     L.append(sol['cost'])
#     E.append(e_budget)
#
#
# print "Construct graph of optimization problem."
# plt.title("Minimization of delay constrained to different energy budgets")
# plt.xlabel("E_budget")
# plt.ylabel("L_min")
# plt.plot(E, L)
# plt.savefig('images/minimize_delay.png')
# plt.clf()
# print "\tDone.\n"




#############
#   TASK 3  #
#############

print "Finding trade-off between energy consumption and latency."

Fs = 1.0/(60*30*1000)
alpha1 = A1+A3*Fs
alpha2 = A4*Fs
alpha3 = A2*Fs

beta1 = 0
for i in range(D):
    beta1 += 1.0/2.0

beta2 = 0
for i in range(D):
    beta2 += (Tcw/2.0)+Tdata


E_worst = alpha1/Tw_min + alpha2*Tw_min + alpha3
L_worst = beta1*Tw_max + beta2

def con0(params):
    E, L, Tw = params
    return E_worst - alpha1/Tw - alpha2*Tw - alpha3

def con1(params):
    E, L, Tw = params
    return E - alpha1/Tw - alpha2*Tw - alpha3

def con2(params):
    E, L, Tw = params
    return L_worst - beta1*Tw - beta2

def con3(params):
    E, L, Tw = params
    return L - beta1*Tw - beta2

def con4(params):
    E, L, Tw = params
    return Tw - Tw_min

def con5(params):
    E, L, Tw = params
    return -(0.25 - (Tcs + Tal + Tw/2.0 + Tack + Tdata) * Fout_d[1] + Fs * C)


cons = ({'type': 'ineq', 'fun': con0},
        {'type': 'ineq', 'fun': con1},
        {'type': 'ineq', 'fun': con2},
        {'type': 'ineq', 'fun': con3},
        {'type': 'ineq', 'fun': con4},
        {'type': 'ineq', 'fun': con5})

def fun(params):
    E, L, Tw = params
    res = -np.log(np.subtract(E_worst, E)) - np.log(np.subtract(L_worst, L))
    return res


initial_guess = [0, 2000, 100] # E, L, Tw
result = minimize(fun, initial_guess, method="SLSQP", constraints=cons)
if result.success:
    print "\tE:", result.x[0]
    print "\tL:", result.x[1]
    print "\tTw:", result.x[2]
    print "\tRes:", result.fun
else:
    raise ValueError(result.message)




#############
#   TASK 4  #
#############

print "\nFinding KSBS point."

E_budget = 0.050
L_max = 2300

E_best = alpha1/Tw_max + alpha2*Tw_max + alpha3
L_best = beta1*Tw_min + beta2

def fun1(params):
    r, x = params
    return -r

def con10(params):
    r, x = params
    return E_budget - alpha1/x - alpha2*x - alpha3

def con11(params):
    r, x = params
    return L_max - beta1*x - beta2

def con12(params):
    r, x = params
    return E_worst - alpha1/x - alpha2*x - alpha3

def con13(params):
    r, x = params
    return L_worst - beta1*x - beta2

def con14(params):
    r, x = params
    return (E_worst - (alpha1/x + alpha2*x + alpha3))/((E_worst-E_best) - r)

def con15(params):
    r, x = params
    return (L_worst - (beta1*x + beta2))/((L_worst-L_best) - r)


cons = ({'type': 'ineq', 'fun': con10},
        {'type': 'ineq', 'fun': con11},
        {'type': 'ineq', 'fun': con12},
        {'type': 'ineq', 'fun': con13},
        {'type': 'eq', 'fun': con14},
        {'type': 'eq', 'fun': con15})

#100000000
initial_guess = [100000000, 250] # r, x
result = minimize(fun1, initial_guess, constraints=cons)

if result.success:
    print "\tr:", result.x[0]
    print "\tTw:", result.x[1]
else:
    raise ValueError(result.message)

print ""
