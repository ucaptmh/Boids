__author__ = 'third'
from Boids.flock import Flock
from Boids.boids import Boids
from argparse import ArgumentParser
import numpy as np
import yaml

def process():

    configdata = yaml.load(open('config.yaml'))

    flock = Flock(
        flock_size=configdata["flock_size"],
        formation_flying_distance=configdata["formation_flying_distance"],
        formation_flying_strength=configdata["formation_flying_strength"],
        alert_distance=configdata["alert_distance"],
        attraction_strength=configdata["attraction_strength"],
        axes_min=configdata["axes_min"],
        axes_max=configdata["axes_max"],
        lower_position_limit=configdata["lower_position_limit"],
        upper_position_limit=configdata["upper_position_limit"],
        lower_velocity_limit=configdata["lower_velocity_limit"],
        upper_velocity_limit=configdata["upper_velocity_limit"],
        frame_number=configdata["frame_number"],
        frame_interval=configdata["frame_interval"])
    """
    flock=Flock()
    """
    boid = Boids(flock, flock.flock_positions(), flock.flock_velocities())
    boid.simulate(show=True)

if __name__ == "__main__":
    process()
