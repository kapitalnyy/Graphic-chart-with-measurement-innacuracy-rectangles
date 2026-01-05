import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

x = [1, 2, 3]
y = [2.1, 2.9, 3.8]
dx = [0.2, 0.15, 0.25]
dy = [0.3, 0.2, 0.35]

fig, ax = plt.subplots()

ax.scatter(x, y, color='black', zorder=3, s=1)

for xi, yi, dxi, dyi in zip(x, y, dx, dy):
    rect = Rectangle(
        (xi - dxi, yi - dyi),   
        2*dxi,                 
        2*dyi,                 
        alpha=0.9,
        edgecolor='blue',
        facecolor='none',
        linewidth=0.5
    )
    ax.add_patch(rect)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Prostokąty niepewności pomiarowych")
ax.grid(True)
ax.margins(2) #change margins to scale the chart 
ax.set_aspect('auto') 

plt.show()
