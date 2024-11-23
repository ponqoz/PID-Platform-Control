import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

class ThreeDPlot:
    def __init__(self):
        self.create_plane()
        self.create_ball()
        self.rotation_angles = {'x': 0, 'y': 0}  # Speichert Rotationswinkel

    # Funktion, um die Anfangsebene zu erstellen
    def create_plane(self):
        x = [0, 10] # Liste mit 0 und 10, Grenzen für die Ebene
        y = [0, 10] # Liste mit 0 und 10, Grenzen für die Ebene
        self.X, self.Y = np.meshgrid(x, y)  # Erstelle ein Meshgrid aus den beiden Listen
        self.Z = np.full_like(self.X, 2, dtype=float)  # Erstelle eine Matrix mit 2 als Wert

    # Funktion, um den Ball zu erstellen
    def create_ball(self):
        self.ball_pos = np.array([5.0, 5.0, 4.0])  # Anfangsposition (x, y, z)
        self.ball_radius = 0.5  # Radius des Balls
        self.ball_velocity = np.array([0.0, 0.0, 0.0])  # Anfangsgeschwindigkeit (x, y, z)

    # Funktion, um die Daten für die Animation zu aktualisieren
    def update(self, frame):
        # Rotationspunkt der Ebene
        center = (5, 5, 2)

        # Aktuelle Rotationswinkel abrufen
        theta_x = np.radians(self.rotation_angles['x'])
        theta_y = np.radians(self.rotation_angles['y'])
        
        # Ebene rotieren
        self.X, self.Y, self.Z = self.rotate_plane(self.X, self.Y, self.Z, center, theta_x, axis='x')
        self.X, self.Y, self.Z = self.rotate_plane(self.X, self.Y, self.Z, center, theta_y, axis='y')

        # Aktualisiere die Ebene
        self.surface.remove()
        self.surface = self.ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis')

        # Aktualisiere den Ball
        self.ball_plot.remove()
        self.ball_plot = self.ax.scatter(*self.ball_pos, color='red', s=100)  # Ball neu zeichnen


    # Funktion, um die 3D-Ebene anzuzeigen
    def plot(self):
        # Erstelle ein neues Fenster
        fig = plt.figure()

        # Erstelle ein 3D-Subplot
        self.ax = fig.add_subplot(111, projection='3d')

        # Setze die Grenzen der Achsen
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.set_zlim(0, 5)

        # Setze die Beschriftungen der Achsen
        self.ax.set_xlabel('X-Achse')
        self.ax.set_ylabel('Y-Achse')
        self.ax.set_zlabel('Z-Achse')

        # Zeichne die anfängliche Ebene
        self.surface = self.ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis')

        # Zeichne den Ball
        self.ball_plot = self.ax.scatter(*self.ball_pos, color='red', s=100)

        # Verbinde die Key-Events mit der Steuerungsfunktion
        fig.canvas.mpl_connect('key_press_event', self.on_key_press)

        # Erstelle die Animation
        ani = FuncAnimation(fig, self.update, frames=100, interval=50, blit=False)

        # Zeige die Animation
        plt.show()


    @staticmethod
    def rotate_plane(X, Y, Z, center, theta, axis='z'):
        """
        Rotiert die Punkte X, Y, Z um einen Punkt `center` um den Winkel `theta` (in Rad) 
        um die angegebene Achse.
        """
        X_shifted = X - center[0]
        Y_shifted = Y - center[1]
        Z_shifted = Z - center[2]

        if axis == 'x':
            R = np.array([[1, 0, 0],
                            [0, np.cos(theta), -np.sin(theta)],
                            [0, np.sin(theta), np.cos(theta)]])
        elif axis == 'y':
            R = np.array([[np.cos(theta), 0, np.sin(theta)],
                            [0, 1, 0],
                            [-np.sin(theta), 0, np.cos(theta)]])
        elif axis == 'z':
            R = np.array([[np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [0, 0, 1]])

        rotated = R @ np.array([X_shifted.ravel(), Y_shifted.ravel(), Z_shifted.ravel()])
        X_rot, Y_rot, Z_rot = rotated.reshape(3, *X.shape)

        # Zurückverschieben
        X_rot += center[0]
        Y_rot += center[1]
        Z_rot += center[2]
        return X_rot, Y_rot, Z_rot

    def on_key_press(self, event):
        """
        Event-Handler für Tasteneingaben, um die Ebene zu steuern.
        """
        if event.key == 'up':
            self.rotation_angles['x'] += 2  # Rotation um die x-Achse
        elif event.key == 'down':
            self.rotation_angles['x'] += -2  # Rotation um die x-Achse
        elif event.key == 'left':
            self.rotation_angles['y'] += -2  # Rotation um die y-Achse
        elif event.key == 'right':
            self.rotation_angles['y'] += 2

if __name__ == '__main__':
    plot = ThreeDPlot()
    plot.plot()
