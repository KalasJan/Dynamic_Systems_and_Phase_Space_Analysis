# Jak vypada fazovy portret Dvojiteho kyvadla (double pendulum)

import numpy as np
import matplotlib.pyplot as plt

# 1) fyzika a analyza

g = 9.81 # gravitace

m1 = 2 # hmotnost kyvadla 1
L1 = 1 # delka kyvadla 1
theta1 = np.radians(45) # pocatecni uhel (v radianech)
omega1 = 2 # uhlova rychlost

m2 = 1 # whmotnost kyvadla 2
L2 = 2 # delka kyvadla 2
theta2 = np.radians(70) # pocatecni uhel (v radianech)
omega2 = 4 # uhlova rychlost

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

# fazovy portret

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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 1. Graf pro první kyvadlo
ax1.plot(stav[:, 0], stav[:, 1], lw=0.8, color="royalblue", label=f"Kyvadlo 1 ($m_1$={m1}, $L_1$={L1})")
ax1.set_title(fr"Fázový portrét 1. kyvadla ($m_1$={m1}, $L_1$={L1})")
ax1.set_xlabel(r"Úhel kyvadla: $\alpha_1$ [rad]")
ax1.set_ylabel(r"Úhlová rychlost: $\dot{\alpha}_1$ [rad/s]")
ax1.grid(True, linestyle='--', alpha=0.5)

# 2. Graf pro druhé kyvadlo
ax2.plot(stav[:, 2], stav[:, 3], lw=0.8, color="crimson", label=f"Kyvadlo 2 ($m_2$={m2}, $L_2$={L2})")
ax2.set_title(fr"Fázový portrét 2. kyvadla ($m_2$={m2}, $L_2$={L2})")
ax2.set_xlabel(r" Úhel kyvadla: $\alpha_2$ [rad]")
ax2.set_ylabel(r"Úhlová rychlost: $\dot{\alpha}_2$ [rad/s]")
ax2.grid(True, linestyle='--', alpha=0.5)

plt.suptitle('Fázové portéty Dynamického systému Dvojité kyvadlo (Double pendulum)', fontsize=15, weight='bold', y=0.96)
plt.tight_layout()
plt.show()