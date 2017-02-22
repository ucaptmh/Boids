__author__ = 'third'
from matplotlib import pyplot as plt
from matplotlib import animation
import random

size_flock = 50
min_x_position, max_x_position = -450, 50
min_y_position, max_y_position = 300, 600
min_x_velocity, max_x_velocity = 0, 10
min_y_velocity, max_y_velocity = -20, 20

attraction_strength = 0.01  # Attraction strength to middle of flock
separation_distance_squared = 100  # Minimum distance squared between boids before they fly apart
velocity_matching_strength = 0.125
nearby_distance_squared = 10000  # Distance squared within which boids will try to match velocities

axes_min, axes_max = -500, 1500

frame_number, frame_interval = 50, 50


class Boids(object):
    def __init__(self):
        boids_x = [random.uniform(min_x_position, max_x_position) for x in range(size_flock)]
        boids_y = [random.uniform(min_y_position, max_y_position) for x in range(size_flock)]
        boid_x_velocities = [random.uniform(min_x_velocity, max_x_velocity) for x in range(size_flock)]
        boid_y_velocities = [random.uniform(min_y_velocity, max_y_velocity) for x in range(size_flock)]
        self.boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

    def update_boids(self, boids):
        xs, ys, xvs, yvs = boids
        # Fly towards the middle
        for i in range(len(xs)):
            for j in range(len(xs)):
                xvs[i] += (xs[j] - xs[i]) * attraction_strength / len(xs)
                yvs[i] += (ys[j] - ys[i]) * attraction_strength / len(xs)
        # Fly away from nearby boids
                if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < separation_distance_squared:
                    xvs[i] = xvs[i] + (xs[i] - xs[j])
                    yvs[i] = yvs[i] + (ys[i] - ys[j])
        # Try to match speed with nearby boids
                if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < nearby_distance_squared:
                    xvs[i] += (xvs[j] - xvs[i]) * velocity_matching_strength / len(xs)
                    yvs[i] += (yvs[j] - yvs[i]) * velocity_matching_strength / len(xs)
        # Move according to velocities
        for i in range(len(xs)):
            xs[i] = xs[i] + xvs[i]
            ys[i] = ys[i] + yvs[i]

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
    boid = Boids()
    boid.simulate()