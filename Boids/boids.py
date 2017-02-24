__author__ = 'third'
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from Boids.flock import Flock


class Boids(object):
    def __init__(self, flock, positions, velocities):
        self.flock = flock
        self.positions = positions
        self.velocities = velocities
        self.boids = (self.positions, self.velocities)

    def update_boids(self):
        #Attracted to middle of flock
        move_to_middle_strength = self.flock.attraction_strength
        middle = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle * move_to_middle_strength
        #Change direction if too close
        separations = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        alert_distance = self.flock.alert_distance_sq
        far_away = square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0, :, :][far_away] = 0
        separations_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(separations_if_close, 1)
        #Similar velocity to neighbours
        velocity_differences = self.velocities[:, np.newaxis, :] - self.velocities[:, :, np.newaxis]
        formation_flying_distance = self.flock.formation_flying_distance_sq
        formation_flying_strength = self.flock.formation_flying_strength
        very_far = square_distances > formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0, :, :][very_far] = 0
        velocity_differences_if_close[1, :, :][very_far] = 0
        self.velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength

        self.positions += self.velocities

    def simulate(self, show=True):
        figure = plt.figure()
        axes = plt.axes(xlim=(self.flock.axes_min, self.flock.axes_max), ylim=(self.flock.axes_min, self.flock.axes_max))
        self.scatter = axes.scatter(self.boids[0], self.boids[1])
        anim = animation.FuncAnimation(figure, self.animate, frames=self.flock.frame_number, interval=self.flock.frame_interval)
        if show:
            plt.title('Boids')
            plt.show()


    def animate(self,frame):
        self.update_boids()
        self.scatter.set_offsets(self.positions.transpose())
"""
if __name__ == "__main__":
    flock=Flock()
    boid=Boids(flock, flock.flock_positions(), flock.flock_velocities())
    boid.simulate(show=True)
"""