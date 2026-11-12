# plot the Fractal tree

import matplotlib.pyplot as plt
import numpy as np

def tree(ax, x, y, angle, length, level):
  if level == 0:
    return

   # actual branch
  x_end = x + length * np.cos(angle)
  y_end = y + length * np.sin(angle)
  
  # plot the branch; slimmer and slimmer
  ax.plot([x, x_end], [y, y_end], color="green", linewidth=level * 0.8)
  
  # angle
  uhel = np.pi/6 # 30 deg angle
  
  tree(ax, x_end, y_end, angle + uhel, length * 0.75, level - 1)
  tree(ax, x_end, y_end, angle - uhel, length * 0.75, level - 1)
  
# plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.axis("off")

tree(ax, x=0, y=0, angle=np.pi / 2, length=100, level=10)

plt.title("Fractal Tree", fontsize=14)
plt.show()