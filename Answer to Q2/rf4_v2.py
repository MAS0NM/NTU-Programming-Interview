''' The four equations are solved in parallel, and the global concentration variables are changed '''

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

def rf4(y, x, dx, func):
    k1 = dx * func(y, x)
    k2 = dx * func(y + k1/2, x + dx/2)
    k3 = dx * func(y + k2/2, x + dx/2)
    k4 = dx * func(y + k3, x + dx)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6.0

if __name__=='__main__':
    dt = 1e-20
    n = 10
    t = 0
    ys, ts = [], []
    ys.append(E)
    ys.append(S)
    ys.append(ES)
    ys.append(P)
    ts.append(t)
    for i in range(n):
        E += rf4(E, t, dt, dE)
        ys.append(E)
        S += rf4(S, t, dt, dS)
        ys.append(S)
        ES += rf4(ES, t, dt, dES)
        ys.append(ES)
        P += rf4(P, t, dt, dP)
        ys.append(P)

        ts.append(t)
        t += dt

    plt.plot(ts[:], ys[::4], label='E')
    plt.plot(ts[:], ys[1::4], label='S')
    plt.plot(ts[:], ys[2::4], label='ES')
    plt.plot(ts[:], ys[3::4], label='P')
    plt.legend()
    plt.show()
