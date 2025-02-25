import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math

# Variablen 
x = 250
y = 250
r = 10
phi = 0
trail_length = 10  # Länge der Leuchtspur
color = 'red'

# Fenster und Diagramm erstellen
fig, ax = plt.subplots()
ax.set_xlabel('x-Koordinate')
ax.set_ylabel('y-Koordinate')
ax.set_title('2D Live Plot')
ax.set_xlim(0, 500)
ax.set_ylim(0, 500)
ax.set_aspect('equal')

# Kreis erstellen
circle = plt.Circle((x, y), r, color=color, alpha=1.0)
# Kreis im Diagramm anzeigen
ax.add_patch(circle)

# Liste für die Spur (Kreise vorbereiten)
trail_patches = [plt.Circle((x, y), r, color=color, alpha=0) for _ in range(trail_length)]
for patch in trail_patches:
    ax.add_patch(patch)  # Alle in die Zeichnung einfügen]

# Animationsfunktion
def update(frame):
    global x
    global y
    global phi 
    phi += 5
    x = math.cos(math.radians(phi)) * 100 + 250
    y = math.sin(math.radians(phi)) * 100 + 250

    circle.set_center((x, y))
    
    # Alle Kreise der Spur aktualisieren
    for i in range(trail_length - 1, 0, -1):
        trail_patches[i].set_center(trail_patches[i - 1].center)
        trail_patches[i].set_alpha(trail_patches[i - 1].get_alpha())

    # Neuesten Punkt zur Spur hinzufügen
    trail_patches[0].set_center((x, y))
    trail_patches[0].set_alpha(0.2)  # Starttransparenz der Spur


ani = animation.FuncAnimation(fig, update, frames=1000,  interval=20)


plt.show()
