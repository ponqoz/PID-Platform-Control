from ursina import *

# Ursina-Anwendung starten
app = Ursina()

# Spieler erstellen
player = Entity(
    model='cube',
    color=color.orange,
    scale=(1, 2, 1),  # Spielergröße
    position=(0, 1, 0),
    collider = 'box'
)

# Wand erstellen
wall = Entity(
    model='cube',
    color=color.red,
    scale=(3, 3, 0.5),  # Größe der Wand
    position=(3, 1.5, 0),  # Position der Wand
    collider='box'  # Collider für die Kollision
)

# Raycast-Visualisierung (optional)
ray_visual = Entity(model='cube', color=color.green, scale=(0.1, 0.1, 1), visible=False)

def update():
    # Raycast von der Position des Spielers in die Blickrichtung
    hit_info = raycast(player.position, player.forward, ignore=[player], distance=5, debug=True)

    # Überprüfen, ob der Raycast etwas trifft
    if hit_info.hit:
        # Ausgabe der getroffenen Entität und Position
        print(f"Getroffen: {hit_info.entity}, Position: {hit_info.world_point}")
        
        # Sichtbare Markierung für die Kollision (optional)
        ray_visual.position = hit_info.world_point
        ray_visual.visible = True
    else:
        ray_visual.visible = False  # Markierung ausblenden, wenn nichts getroffen wurde

    # Spieler mit WASD bewegen
    player.position += Vec3(
        held_keys['d'] - held_keys['a'],  # Seitwärtsbewegung
        0,                               # Keine Bewegung in Y-Richtung
        held_keys['w'] - held_keys['s']  # Vorwärts-/Rückwärtsbewegung
    ) * time.dt * 5

# Ursina-Anwendung ausführen
app.run()
