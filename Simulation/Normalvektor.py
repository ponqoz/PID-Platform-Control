import math
import numpy as np

def berechne_normalvektor():
    # Winkel in Grad
    phi = 0  # Drehwinkel um die Z-Achse
    psi = 0    # Drehwinkel um die Y-Achse
    theta = 0    # Drehwinkel um die X-Achse

    # Umwandlung der Winkel in Bogenmaß
    theta_rad = math.radians(theta)
    phi_rad = math.radians(phi)
    psi_rad = math.radians(psi)

    # Vektor (0, 1, 0)
    v = np.array([0, 0, 1])

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


    print("Neuer Vektor:", v_prime)
