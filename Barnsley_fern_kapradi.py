# Plot the fractal - Barnsley fern

import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_pts = 100000
x = np.zeros(n_pts)
y = np.zeros(n_pts)

# Generate random probabilities at once (faster than calling random inside the loop)
r = np.random.random(n_pts)

# Chaos game iteration
for i in range(1, n_pts):
    if r[i] < 0.01:
        # f1: stem (1 %)
        x[i] = 0.0
        y[i] = 0.16 * y[i - 1]
    elif r[i] < 0.86:
        # f2: successively smaller leaflets (85 %)
        x[i] = 0.85 * x[i - 1] + 0.04 * y[i - 1]
        y[i] = -0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6
    elif r[i] < 0.93:
        # f3: largest left-hand leaflet (7 %)
        x[i] = 0.20 * x[i - 1] - 0.26 * y[i - 1]
        y[i] = 0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6
    else:
        # f4: largest right-hand leaflet (7 %)
        x[i] = -0.15 * x[i - 1] + 0.28 * y[i - 1]
        y[i] = 0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44

# Plotting
fig, ax = plt.subplots(figsize=(6, 10))
ax.scatter(x, y, s=0.2, color='forestgreen', edgecolors='none')

ax.set_aspect('equal')
ax.axis('off')
plt.title(f"Barnsley fern ({n_pts:,} points)")
plt.tight_layout()
plt.show()


# version 2 - Colored by iteration depth

# Parameters
n_points = 150000
x2 = np.zeros(n_points)
y2 = np.zeros(n_points)
depth = np.zeros(n_points)  # Tracks the iteration depth (level)

# Generate random probabilities
rk = np.random.random(n_points)

# Chaos game iteration
for j in range(1, n_points):
    if rk[j] < 0.01:
        # f1: stem (resets depth to 0)
        x2[j] = 0.0
        y2[j] = 0.16 * y2[j - 1]
        depth[j] = 0
    elif rk[j] < 0.86:
        # f2: successively smaller leaflets
        x2[j] = 0.85 * x2[j - 1] + 0.04 * y2[j - 1]
        y2[j] = -0.04 * x2[j - 1] + 0.85 * y2[j - 1] + 1.6
        depth[j] = depth[j - 1] + 1
    elif rk[j] < 0.93:
        # f3: largest left-hand leaflet
        x2[j] = 0.20 * x2[j - 1] - 0.26 * y2[j - 1]
        y2[j] = 0.23 * x2[j - 1] + 0.22 * y2[j - 1] + 1.6
        depth[j] = depth[j - 1] + 1
    else:
        # f4: largest right-hand leaflet
        x2[j] = -0.15 * x2[j - 1] + 0.28 * y2[j - 1]
        y2[j] = 0.26 * x2[j - 1] + 0.24 * y2[j - 1] + 0.44
        depth[j] = depth[j - 1] + 1

# Plotting
fig2, ax2 = plt.subplots(figsize=(7, 10))

# vmin/vmax limits the color scale so the first ~25 levels are clearly visible
sc = ax2.scatter(x2, y2, c=depth, cmap='viridis', s=0.3, edgecolors='none', vmin=0, vmax=25)

plt.colorbar(sc, ax=ax2, label='Iteration depth (steps from stem)', shrink=0.7)
ax2.set_aspect('equal')
ax2.axis('off')
plt.title(f"Barnsley fern colored by iteration depth ({n_points:,} points)")
plt.tight_layout()
plt.show()