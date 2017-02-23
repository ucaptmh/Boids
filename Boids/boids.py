from matplotlib import pyplot as plt
from matplotlib import animation
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
    def __init__(self, positions, velocities):
        self.positions = positions
        self.velocities = velocities
        self.boids = (self.positions, self.velocities)



    def update_boids(self, positions, velocities):
        move_to_middle_strength = 0.01
        middle = np.mean(positions, 1)
        direction_to_middle = positions-middle[:,np.newaxis]
        velocities -= direction_to_middle*move_to_middle_strength

        separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
        squared_displacements = separations*separations
        square_distances = np.sum(squared_displacements, 0)
        alert_distance = 100
        far_away=square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] =0
        separations_if_close[1,:,:][far_away] =0
        velocities += np.sum(separations_if_close,1)

        velocity_differences = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
        formation_flying_distance = 10000
        formation_flying_strength = 0.125
        very_far=square_distances > formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] =0
        velocity_differences_if_close[1,:,:][very_far] =0
        velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength

        positions += velocities

    def simulate(self, show=True):
        figure = plt.figure()
        axes = plt.axes(xlim=(axes_min, axes_max), ylim=(axes_min, axes_max))
        self.scatter = axes.scatter(self.boids[0], self.boids[1])
        anim = animation.FuncAnimation(figure, self.animate, frames=frame_number, interval=frame_interval)
        if show:
            plt.show()


    def animate(self,frame):
        self.update_boids(positions, velocities)
        self.scatter.set_offsets(positions.transpose())


def new_flock(count, lower_limits, upper_limits):
    width=upper_limits-lower_limits
    return (lower_limits[:,np.newaxis] +
         np.random.rand(2,count)*width[:,np.newaxis])


if __name__ == "__main__":
    positions=new_flock(flock_size, np.array([min_x_position,min_y_position]), np.array([max_x_position,max_y_position]))
    velocities=new_flock(flock_size, np.array([min_x_velocity,min_y_velocity]), np.array([max_x_velocity,max_y_velocity]))
    boid = Boids(positions,velocities)
    boid.simulate()