# Project 1. Duty-Cycle MAC Protocols - Energy Conservation


## Q1

#### Construct Topology
The first requirement is to construct an arbitrary topology of nodes. This is done by running
the script *IoT-GT-header.py* provided by prof. Ordinas.

The constructed topology has the following properties:
- Insert topology here.
- (Maybe even draw a graph visualizing the topology).

#### Calculate Values
In order to calculate the estimated energy conservation and the end-to-end delay of packet
transmission, the script *calculation.py* is constructed. This script inputs a
set of variables for different properties of the network, and calculates the results according to
the formulas provided by the project pdf document, *Table 2* respectively.

#### Draw Curves
By inserting the aforementioned set of values into the constructed script, results for energy consumption and overall network latency is obtained Consequently, a variety of curves can be drawn in order to see the relationsships between the different elements.

**Energy as a function of sleep time**
![Energy0](images/energy0.png)
![Energy0](images/energy1.png)
![Energy0](images/energy2.png)
![Energy0](images/energy3.png)
For our specified time interval Tw in [100, 500], the curvature of the slope is approximately a negative exponential function when packets are generated at a relatively slow pace. However, as the packet generation increases, we see that the energy also starts to gradually increase when the sleeping time increases.

**Delay as a function of sleep time**
![Delay0](images/delay0.png)
![Delay1](images/delay1.png)
![Delay2](images/delay2.png)
![Delay3](images/delay3.png)
The curve is increasing in a linear scale. The slope remains the same for each test, as a result of not being affected by the sampling rate.

**Delay as a function of energy**:
![Energy-delay0](images/energy_delay0.png)
![Energy-delay0](images/energy_delay1.png)
![Energy-delay0](images/energy_delay2.png)
![Energy-delay0](images/energy_delay3.png)
The graph with the slowest packet generation shows that there is a significant relationship between energy and delay; the energy consumption is high when the delay is low and vica versa. However, when increasing the packet sampling generation frequency, it isn't necessarily the case that the highest delay is equivalent to the lowest energy consumption.

The graphs of the energy vs. delay yields that there is a specific point when the delay starts increasing, as well as the energy consumption is increasing. This is a result of the waiting time is getting very large. Consequently, strobes will repeatedly be sent, whereas none of them will be acknowledged. Therefore, both energy and the delay will increase.

When the sampling rate is very high, we find ourselves in a case where our model is simply not suitable anymore. That would correspond to a scenario where the sleeping time is higher than the sampling interval. This results in graphs that makes no sense.




## Q2
For the optimization problems that are presented in the project, we choose to use Python with library gpkit with coherent dependencies.

**Minimize energy consumption subject to some maximum delay**
![Minimize_energy](minimize_energy.png)

The graph yields that for an *Lmax* value lower than roughly 1800 ms, the minimal energy consumption increases exponentially. At the same time, we also see that there is no benefit in increasing the maximum delay, in terms of reduced energy consumption.

**Minimize delay subject to some energy budget**
![Minimize_delay](minimize_delay.png)

For the minimization of delay instead of energy, the same pattern occurs. There is a specific point for e_budget of around 0.038 where a lower budget will significantly increase the delay, and likewise, a higher energy budget will not improve it.

It interesting to notice that for both scenarios, there is a specific point where increasing one variable do not affect the other variable in any noticable way. This means that we certaintly can make usage of optimization techniques in order to find the best possible trade-off between the mentioned variables and therefore the system as a whole. 




## Q3
- Find trade-off - solve optimization problem





## Q4
- Use Kalai-Smorodinsky Bargaining Solution (KSBS) to find equal proportion of gain between
players.
