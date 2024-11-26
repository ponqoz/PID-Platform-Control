
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Ursina-Anwendung starten
app = Ursina()

# Konstanten
gravitation = Vec3(0, -9.81, 0) # Gravitationskonstante in m/s²
mass_ball = 0.02  # Masse des Balls in kg
ball_velocity = Vec3(0, 0, 0)  # Geschwindigkeit des Balls in m/s

# Eine Ebene (Plane) mit einer Höhe von 1 erstellen
plane = Entity(
    model='cube',
    color=color.white,
    scale=(10, 3, 10),  # (Breite, Höhe, Tiefe)
    position=(0, 0, 0),
    collider='box'
)

# Ball erstellen
ball = Entity(
    model='sphere',
    color=color.red,
    scale=1,  # Durchmesser des Balls
    position=(0, 10, 0),  # Startposition des Balls
    collider='box'
)

# Raycast-Visualisierung (optional)
ray_visual = Entity(model='cube', color=color.green, scale=(0.1, 0.1, 1), visible=False)

def update():
    global ball_velocity
    directions = {
        "forward": Vec3(0, 0, 1),
        "backward": Vec3(0, 0, -1),
        "left": Vec3(-1, 0, 0),
        "right": Vec3(1, 0, 0),
        "up":  Vec3(0, 1, 0).normalized(),
        "down": Vec3(0, -1, 0).normalized(),
    }
    # Welt-Normale berechnen
    current_normal_vector_plane = plane.world_rotation @ Vec3(Vec3(0, -1, 0))

    direction = Vec3(directions['up'] * (held_keys['i'] - held_keys['k']))
    
    #for direction_name, direction_vector in directions.items():
    # Raycast von der Position des Spielers in die Blickrichtung
    hit_info = raycast(ball.position, current_normal_vector_plane, ignore=[ball], distance=0.5, debug=True)

    if not hit_info.hit:
        # Geschwindigkeit aktualisieren: v = v0 + g * t
        ball_velocity += gravitation * time.dt
        # Position aktualisieren: y = y0 + v * t
        ball.position += current_normal_vector_plane * time.dt * 5


# First-Person-Steuerung
player = FirstPersonController()
player.gravity = 0  # Gravitation für den Spieler deaktivieren
player.speed = 10
player.position = (0, 1, -10)
player.look_at(ball)

# Ursina-Anwendung ausführen
app.run()
