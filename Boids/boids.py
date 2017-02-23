__author__ = 'third'
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class Boids(object):
    def __init__(self, positions, velocities):
        self.flock = flock

        self.positions = positions
        self.velocities = velocities
        self.boids = (self.positions, self.velocities)

    def update_boids(self):
        move_to_middle_strength = self.flock.attraction_strength
        middle = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle * move_to_middle_strength

        separations = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        alert_distance = self.flock.alert_distance_sq
        far_away = square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0, :, :][far_away] = 0
        separations_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(separations_if_close, 1)

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
            plt.show()


    def animate(self,frame):
        self.update_boids()
        self.scatter.set_offsets(self.positions.transpose())


class Flock(object):
    def __init__(self,
                 flock_size=50,
                 formation_flying_distance=100,
                 formation_flying_strength=0.125,
                 alert_distance=10,
                 attraction_strength=0.01,
                 axes_min=-500,
                 axes_max=1500,
                 lower_position_limit=np.array([-450, 300]),
                 upper_position_limit=np.array([50, 600]),
                 lower_velocity_limit=np.array([0, -20]),
                 upper_velocity_limit=np.array([10, 20]),
                 frame_number=50,
                 frame_interval=50):


        self.formation_flying_distance_sq = formation_flying_distance ** 2
        self.formation_flying_strength = formation_flying_strength
        self.alert_distance_sq = alert_distance ** 2
        self.attraction_strength = attraction_strength
        self.axes_min = axes_min
        self.axes_max = axes_max
        self.flock_size = flock_size
        self.lower_position_limit = lower_position_limit
        self.upper_position_limit = upper_position_limit
        self.lower_velocity_limit = lower_velocity_limit
        self.upper_velocity_limit = upper_velocity_limit
        self.frame_number = frame_number
        self.frame_interval = frame_interval
        self.boids = (self.flock_positions(), self.flock_positions())

    def new_flock(self, lower_limits, upper_limits):
        width = upper_limits - lower_limits
        return (lower_limits[:, np.newaxis] +
                np.random.rand(2, self.flock_size) * width[:, np.newaxis])

    def flock_positions(self):
        return self.new_flock(self.lower_position_limit,
                              self.upper_position_limit)

    def flock_velocities(self):
        return self.new_flock(self.lower_velocity_limit,
                              self.upper_velocity_limit)


if __name__ == "__main__":
    flock=Flock()
    boid=Boids(flock.flock_positions(), flock.flock_velocities())
    boid.simulate(show=True)
