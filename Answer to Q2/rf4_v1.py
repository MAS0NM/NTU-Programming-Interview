''' The four equations are solved sequentially, the global concentration variables are not changed'''

import matplotlib.pyplot as plt

E = 1; S = 10; ES = 0; P = 0;
k1 = 100; k2 = 600; k3 = 150

def dE(t, E):
    return (k2 + k3)*ES - k1*E*S

def dS(t, S):
    return k2*ES - k1*E*S

def dES(t, ES):
    return k1 * E * S - (k2 + k3) * ES

def dP(t, P):
    return k3*ES

def runge_kutta(y, x, dx, func):
    k1 = dx * func(y, x)
    k2 = dx * func(y + k1/2, x + dx/2)
    k3 = dx * func(y + k2/2, x + dx/2)
    k4 = dx * func(y + k3, x + dx)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6.0

if __name__=='__main__':
    dt = 0.1
    n = 10
    ys, ts = [], []
    funcList = [(dE, E), (dS, S), (dES, ES), (dP, P)]
    for (func, y) in funcList:
        t = 0.0
        for i in range(n):
            y = runge_kutta(y, t, dt, func)
            t += dt
            ys.append(y)
            ts.append(t)

    plt.plot(ts[:n-1], ys[:n-1], label='E')
    plt.plot(ts[n:2*n-1], ys[n:2*n-1], label='S')
    plt.plot(ts[2*n:3*n-1], ys[2*n:3*n-1], label='ES')
    plt.plot(ts[3*n:4*n-1], ys[3*n:4*n-1], label='P')
    plt.legend()
    plt.show()
