__author__ = 'third'
import numpy as np


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