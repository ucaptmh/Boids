from Boids.boids import Boids
from Boids.boids import Flock
import numpy as np
from numpy.testing import assert_array_less
import os
import yaml
from mock import patch

def test_boids_regression():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures', 'regression_fixture.yml')))
    boid_data = regression_data["before"]
    boids = Boids(Flock(), boid_data[0], boid_data[1])
    boids.update_boids()

    for after, before in zip((regression_data["after"][0], regression_data["after"][1]), boid_data):
        for after_value, before_value in zip(after, before):
            np.testing.assert_array_almost_equal(after_value, before_value)


def test_boids_init():
    flock = Flock(flock_size=2,
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
                  frame_interval=50)
    boid = Boids(flock, [1, 2, 3, 4], [3, 4, 5, 6])
    # check Boid reads from Flock, and the positions and velocities are read correctly
    np.testing.assert_equal(flock.flock_size, 2)
    np.testing.assert_equal(flock.formation_flying_distance_sq,10000)
    np.testing.assert_equal(boid.positions, [1, 2, 3, 4])
    np.testing.assert_equal(boid.velocities, [3, 4, 5, 6])



def test_boids_update_boids():
    update_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures', 'update_fixture.yml')))
    boid_data = update_data["before"]
    boids = Boids(Flock(), boid_data[0], boid_data[1])
    boids.update_boids()
    for after, before in zip((update_data["after"][0], update_data["after"][1]), boid_data):
        for after_value, before_value in zip(after, before):
            np.testing.assert_array_almost_equal(after_value, before_value)