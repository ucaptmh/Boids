__author__ = 'third'
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np


min_x_position, max_x_position = -450, 50
min_y_position, max_y_position = 300, 600
min_x_velocity, max_x_velocity = 0, 10
min_y_velocity, max_y_velocity = -20, 20

axes_min, axes_max = -500, 1500

flock_size = 50
attraction_strength = 0.01  # Attraction strength to middle of flock
separation_distance_squared = 100  # Minimum distance squared between boids before they fly apart
velocity_matching_strength = 0.125
nearby_distance_squared = 10000  # Distance squared within which boids will try to match velocities



frame_number, frame_interval = 50, 50



class Boids(object):
    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.boids = (self.x_position, self.y_position, self.x_velocity, self.y_velocity)


    def update_boids(self, boids):
        x_position, y_position, x_velocity, y_velocity = boids
        # Fly towards the middle
        for i in range(flock_size):
            for j in range(flock_size):
                x_position_difference = x_position[j] - x_position[i]
                y_position_difference = y_position[j] - y_position[i]
                x_velocity_difference = x_velocity[j] - x_velocity[i]
                y_velocity_difference = y_velocity[j] - y_velocity[i]

                x_velocity[i] += x_position_difference * attraction_strength / flock_size
                y_velocity[i] += y_position_difference * attraction_strength / flock_size
                # Fly away from nearby boids
                if x_position_difference ** 2 + y_position_difference ** 2 < separation_distance_squared:
                    x_velocity[i] = x_velocity[i] + (x_position[i] - x_position[j])
                    y_velocity[i] = y_velocity[i] + (y_position[i] - y_position[j])
                    # Try to match speed with nearby boids
                if x_position_difference ** 2 + y_position_difference ** 2 < nearby_distance_squared:
                    x_velocity[i] += x_velocity_difference * velocity_matching_strength / flock_size
                    y_velocity[i] += y_velocity_difference * velocity_matching_strength / flock_size
        # Move according to velocities
        for i in range(flock_size):
            x_position[i] += x_velocity[i]
            y_position[i] += y_velocity[i]

    def simulate(self, show=True):
        figure = plt.figure()
        axes = plt.axes(xlim=(axes_min, axes_max), ylim=(axes_min, axes_max))
        self.scatter = axes.scatter(self.boids[0], self.boids[1])
        anim = animation.FuncAnimation(figure, self.animate, frames=frame_number, interval=frame_interval)
        if show:
            plt.show()


    def animate(self, frame):
        self.update_boids(self.boids)
        self.scatter.set_offsets(list(zip(self.boids[0], self.boids[1])))


if __name__ == "__main__":
    boids_x = np.array([random.uniform(min_x_position, max_x_position) for x in range(flock_size)])
    boids_y = np.array([random.uniform(min_y_position, max_y_position) for x in range(flock_size)])
    boid_x_velocity = np.array([random.uniform(min_x_velocity, max_x_velocity) for x in range(flock_size)])
    boid_y_velocity = np.array([random.uniform(min_y_velocity, max_y_velocity) for x in range(flock_size)])
    boid = Boids(boids_x, boids_y, boid_x_velocity, boid_y_velocity)
    boid.simulate()