__author__ = 'third'
from Boids.flock import Flock
from Boids.boids import Boids
from argparse import ArgumentParser
import numpy as np
import yaml


def process():
    def parse_args():
        parser = ArgumentParser(description="Runs boids.")

        parser.add_argument('--file', type=str,
                            help='''Optional YAML file to load data from.
                            Replaces all other specified parameters.''')
        parser.add_argument('--size', default=50, type=int,
                            help='Number of boids in flock. Must be int.')
        parser.add_argument('--flying_distance', default=100, type=float,
                            help='Radius in which boids try and match speed.')
        parser.add_argument('--flying_strength', default=0.125, type=float,
                            help='How strongly boids try and match speed.')
        parser.add_argument('--alert_distance', default=10, type=float,
                            help='Radius in which boids avoid each other.')
        parser.add_argument('--attraction_strength', default=0.01, type=float,
                            help='How strongly boids try and flock together.')
        arguments = parser.parse_args()

        axes_min=-500
        axes_max=1500
        lower_position_limit=np.array([-450, 300])
        upper_position_limit=np.array([50, 600])
        lower_velocity_limit=np.array([0, -20])
        upper_velocity_limit=np.array([10, 20])
        frame_number=50,
        frame_interval=50

        configdata = {"from_file": arguments.file,
                      "flock_size": arguments.size,
                      "formation_flying_distance": arguments.flying_distance,
                      "formation_flying_strength": arguments.flying_strength,
                      "alert_distance": arguments.alert_distance,
                      "attraction_strength": arguments.attraction_strength,
                      "axes_min": axes_min,
                      "axes_max": axes_max,
                      "lower_position_limit": lower_position_limit,
                      "upper_position_limit": upper_position_limit,
                      "lower_velocity_limit": lower_velocity_limit,
                      "upper_velocity_limit": upper_velocity_limit,
                      "frame_number": frame_number,
                      "frame_interval": frame_interval}
        return configdata


    def load_config(config_filename):
        configdata = yaml.load(open('config.yaml'))
        configdata['from_file'] = config_filename
        return configdata

    configdata = parse_args()
    if configdata["from_file"]:
        configdata = load_config(configdata["from_file"])

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
