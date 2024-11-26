from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
import numpy as np

app = Ursina()

# Erstelle einen Würfel
cube = Entity(model='cube', position=(0, 0, 0), rotation=(0, 0, 0))

# Erstelle den Normal-Vektor
origin = Vec3(0, 0, 0)
normal_vector = Vec3(0, 1, 0)
line = Entity(model=Mesh(vertices=[origin, normal_vector], mode='line', thickness=2), color=color.red)
"""
def update():
    # Winkel in Grad holen
    theta_x = math.radians(cube.rotation_x_getter())
    theta_z = math.radians(cube.rotation_z_getter())
    print(theta_x, theta_z)
    
    # Berechnung des Normalvektors
    normal_vector = Vec3(
         math.sin(theta_x),  # x-Komponente
         math.cos(theta_x),  # y-Komponente
         math.sin(theta_z)   # z-Komponente
    )
    
    # Aktualisiere die Linie
    line.model.vertices[1] = normal_vector
    line.model.generate()

    # Würfelrotation
    cube.rotation += (0.5, 0, 0)

"""

def update():
    # Winkel in Grad
    #phi = cube.rotation_z_getter()  # Drehwinkel um die Z-Achse
    #psi = cube.rotation_y_getter()    # Drehwinkel um die Y-Achse
    #theta = cube.rotation_x_getter()    # Drehwinkel um die X-Achse

    # Winkel in Grad
    psi = -cube.rotation_z_getter()
    print(psi)  # Drehwinkel um die Z-Achse
    phi = cube.rotation_y_getter()
    print(phi)    # Drehwinkel um die Y-Achse
    theta = cube.rotation_x_getter()
    print(theta)    # Drehwinkel um die X-Achse

    # Umwandlung der Winkel in Bogenmaß
    theta_rad = math.radians(theta)
    phi_rad = math.radians(phi)
    psi_rad = math.radians(psi)

    # Vektor (0, 1, 0)
    v = np.array([0, 1, 0])

    # Gegebene Matrix (kombinierte Drehmatrix)
    R = np.array([
        [math.cos(psi_rad) * math.cos(phi_rad) - math.cos(theta_rad) * math.sin(phi_rad) * math.sin(psi_rad),
        -math.sin(psi_rad) * math.cos(phi_rad) - math.cos(theta_rad) * math.sin(phi_rad) * math.cos(psi_rad),
        math.sin(theta_rad) * math.sin(phi_rad)],
        
        [math.cos(psi_rad) * math.sin(phi_rad) + math.cos(theta_rad) * math.cos(phi_rad) * math.sin(psi_rad),
        -math.sin(psi_rad) * math.sin(phi_rad) + math.cos(theta_rad) * math.cos(phi_rad) * math.cos(psi_rad),
        -math.sin(theta_rad) * math.cos(phi_rad)],
        
        [math.sin(psi_rad) * math.sin(theta_rad),
        math.cos(psi_rad) * math.sin(theta_rad),
        math.cos(theta_rad)]
    ])

    # Matrix-Vektor-Multiplikation
    v_prime = np.dot(R, v)
    
    # Berechnung des Normalvektors
    normal_vector = Vec3(
         v_prime[0],  # x-Komponente
         v_prime[1],  # y-Komponente
         v_prime[2]   # z-Komponente
    )
    # Aktualisiere die Linie
    line.model.vertices[1] = normal_vector
    line.model.generate()

    # Würfelrotation
    cube.rotation += (0, 0.5, 0)
    #time.sleep(0.5)



    #print("Normalvektor:", v_prime)

# First-Person-Steuerung
player = FirstPersonController()
player.gravity = 0  # Gravitation für den Spieler deaktivieren
player.speed = 10
player.position = (0, 1, -10)

app.run()
