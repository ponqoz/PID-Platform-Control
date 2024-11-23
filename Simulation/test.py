from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Ursina-Anwendung starten
app = Ursina()

# Konstanten
g = 9.81  # Gravitationskonstante in m/s²
m = 0.02  # Masse des Balls in kg

# Eine Ebene (Plane) mit einer Höhe von 1 erstellen
plane = Entity(
    model='cube',
    color=color.white,
    scale=(10, 0.5, 10),  # (Breite, Höhe, Tiefe)
    position=(0, 0, 0),
    collider='box'
)

# Ball erstellen
ball = Entity(
    model='sphere',
    color=color.red,
    scale=1,  # Durchmesser des Balls
    position=(0, 2, 0),  # Startposition des Balls
    collider='sphere'
)

# Variablen für die Ballphysik
ball_velocity = Vec3(0, 0, 0)  # Ballgeschwindigkeit (x, y, z)
ball_gravity = Vec3(0, -g, 0)  # Gravitationskraft auf den Ball (nur in y-Richtung)

def update():
    global ball_velocity

    # Gravitationskraft anwenden
    ball_velocity += ball_gravity * time.dt  # Beschleunigung durch Gravitation

    # Ballposition basierend auf der Geschwindigkeit aktualisieren
    ball.position += ball_velocity * time.dt

    direction = Vec3(
    forward * (held_keys['w'] - held_keys['s'])
    + self.right * (held_keys['d'] - held_keys['a'])
    ).normalized()  # get the direction we're trying to walk in.

    origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
    hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
    if not hit_info.hit:
        self.position += self.direction * 5 * time.dt


# First-Person-Steuerung
player = FirstPersonController()
player.gravity = 0  # Gravitation für den Spieler deaktivieren
player.speed = 10
player.position = (0, 1, -10)
player.look_at(ball)

# Ursina-Anwendung ausführen
app.run()
