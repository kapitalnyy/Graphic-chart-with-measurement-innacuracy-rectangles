import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

x = [1, 2, 3, 4]
y = [2.1, 2.9, 3.8, 5.2]


dx = 0.5  
dy = 0.3  

fig, ax = plt.subplots()
ax.scatter(x, y, s=2, color='black', zorder=3)

for xi, yi in zip(x, y):
    rect = Rectangle(
        (xi - dx/2, yi - dy/2), 
        dx,
        dy,
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
