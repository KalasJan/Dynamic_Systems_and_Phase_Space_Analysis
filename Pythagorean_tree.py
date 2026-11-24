# Plot the fractal - Pythagorean tree

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

# define the tree
def tree(A, B, depth, max_depth, angle, patch, level):
    if depth > max_depth:
        return
    
    # start with square ABCD
    u = B - A
    v = np.array([-u[1], u[0]])  # orthogonal to vector u
    
    D = A + v
    C = B + v
    
    # save this square ABCD (for plot)
    patch.append(Polygon([A, B, C, D], closed=True))
    level.append(depth)
    
    # Triangle CDE, right angle at E
    # |DE| = |u| * cos(fi)
    E = D + np.cos(angle) * (np.cos(angle) * u + np.sin(angle) * v)
    
    # recursion: Left (D->E) and Right (E -> C)
    tree(D, E, depth + 1, max_depth, angle, patch, level)
    tree(E, C, depth + 1, max_depth, angle, patch, level)
    
# parameters
max_depth = 10
angle = np.radians(45) # 45 gives a symmetric tree

patch = []
level = []

# starting coordinates
A = np.array([0.0, 0.0])
B = np.array([1.0, 0.0])

tree(A, B, 0, max_depth, angle, patch, level)

# plotting
fig, ax = plt.subplots(figsize=(10, 8))

# PatchCollection - faster plotting
collection = PatchCollection(patch, cmap='viridis', edgecolor='black', linewidth=0.3)
collection.set_array(np.array(level))
ax.add_collection(collection)

ax.autoscale_view()
ax.set_aspect('equal')
ax.axis('off')
plt.title(f"Pythagorean tree (angle {np.degrees(angle):.0f}°, depth {max_depth})")
plt.tight_layout()
plt.show()