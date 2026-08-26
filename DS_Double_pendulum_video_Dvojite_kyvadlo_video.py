# Jak vypada fazovy portret Dvojiteho kyvadla (double pendulum)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1) fyzika a analyza

g = 9.81 # gravitace

m1 = 2.01 # hmotnost kyvadla 1
L1 = 1 # delka kyvadla 1
theta1 = np.radians(45) # pocatecni uhel (v radianech)
omega1 = 35 # uhlova rychlost

m2 = 1 # whmotnost kyvadla 2
L2 = 2 # delka kyvadla 2
theta2 = np.radians(70) # pocatecni uhel (v radianech)
omega2 = 35 # uhlova rychlost

def double_pendulum(state, m1, m2, l1, l2, g):
    theta1, omega1, theta2, omega2 = state
    
    delta = theta1 - theta2
    
    #zjednodusena derivace, jmenovatel, 
    den = (l1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))
    
    # derivace uhlu
    dt1 = omega1
    dt2 = omega2
    
    # derivace uhlove rychlosti
    num1 = -g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(delta) * m2 * (omega2**2 * l2 + omega1**2 * l1 * np.cos(delta))
    do1 = num1 / den
    
    num2 = 2 * np.sin(delta) * (omega1**2 * l1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + omega2**2 * l2 * m2 * np.cos(delta))
    do2 = num2 / den
    
    return np.array([dt1, do1, dt2, do2])

# 2) animace

dt = 0.01 # delka casoveho kroku
kroku = 3000 # pocet kroku

# zacatek
stav = np.empty((kroku + 1, 4))
stav[0] = [theta1, omega1, theta2, omega2]

for p in range(kroku):
    derivatives = double_pendulum(stav[p], m1, m2, L1, L2, g)
    stav[p + 1] = stav[p] + derivatives * dt

# prevod na kartezsky (x,y) system druheho kyvadla
x2 = L1 * np.sin(stav[:, 0]) + L2 * np.sin(stav[:, 2])
y2 = -L1 * np.cos(stav[:, 0]) - L2 * np.cos(stav[:, 2])

# 3) animace
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-(L1 + L2) * 1.2, (L1 + L2) * 1.2)
ax.set_ylim(-(L1 + L2) * 1.2, (L1 + L2) * 1.2)
ax.set_aspect('equal')
fig.suptitle("Trajektorie dvojiteho kyvadla (Double Pendulum)")
ax.set_title(fr'Kyvadlo 1: $m_1$={m1}, $L_1$={L1}' + '\n' + fr'Kyvadlo 2: $m_2$={m2}, $L_2$={L2}' , fontsize=10, color='gray')
ax.axis('off')

# Samotna kyvadla
(trace,) = ax.plot([], [], lw=0.8, color="royalblue")
(pendulum_lines,) = ax.plot([], [], 'o-', lw=2, color="crimson", ms=6)

# aktualizace snimku
def current(snimek):
    t1_cur = stav[snimek, 0]
    t2_cur = stav[snimek, 2]
    
    x1 = L1 * np.sin(t1_cur)
    y1 = -L1 * np.cos(t1_cur)
    x_end = x1 + L2 * np.sin(t2_cur)
    y_end = y1 - L2 * np.cos(t2_cur)
    
    # kyvadlo [0,0] -> L1 -> L2
    pendulum_lines.set_data([0, x1, x_end], [0, y1, y_end])
    
    # stopa (vykyv soustavy)
    trace.set_data(x2[:snimek], y2[:snimek])
    
    return trace, pendulum_lines

animace_obj = animation.FuncAnimation(
    fig,
    current,
    frames=range(1, kroku + 1, 3),
    interval=15,
    blit=True,
    repeat=False,
)

plt.show()