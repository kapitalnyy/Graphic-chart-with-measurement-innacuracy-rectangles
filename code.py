import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

x = [1,2,10]
y = [1,2,10]


fig, ax = plt.subplots()
ax.scatter(x, y, s=2, color='black', zorder=3)

for xi, yi in zip(x, y):
    dx = 0.01*xi + 0.12
    dy = 0.008*yi + 0.1
    rect = Rectangle(
        (xi - dx, yi - dy), 
        2*dx,
        2*dy,
        linewidth=0.8,
        edgecolor='blue',
        facecolor='none',
        zorder=2
    )
    ax.add_patch(rect)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Prostokąty stałej wielkości")
ax.grid(True)


ax.margins(0.5) #change margins to scale the chart 
ax.set_aspect('auto') 

plt.show()
