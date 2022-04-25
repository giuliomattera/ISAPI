import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initialization
T_START, T_STOP, TS  = 0, 40, 0.1
# Initial condition
X0 = [0,0]
t = np.arange(T_START, T_STOP+1, TS)
# Function that returns dx/dt
def msd_dynamics(x, t):
    
    c = 4 # Damping constant
    k = 2 # Stiffness of the spring
    m = 20 # Mass
    F = 5
    
    dx1dt = x[1]
    dx2dt = (F - c*x[1] - k*x[0])/m
    
    dxdt = [dx1dt, dx2dt]
    
    return dxdt

# Solve ODE
x = odeint(msd_dynamics, X0, t)


x1 = x[:,0]
x2 = x[:,1]

# Plot the Results
plt.plot(t,x1)
plt.plot(t,x2)
plt.title('Simulation of Mass-Spring-Damper System')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(["x1", "x2"])
plt.grid()
plt.show()