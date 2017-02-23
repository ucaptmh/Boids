from Boids.boids import Boids
import numpy as np
import os
import yaml
from Boids.boids import Flock

def test_bad_boids_regression():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures', 'fixture.yml')))
    boid_data = regression_data["before"]
    boids = Boids(Flock(),boid_data[0],boid_data[1])
    boids.update_boids()

    for after, before in zip((regression_data["after"][0],regression_data["after"][1]), boid_data):
        for after_value, before_value in zip(after, before):
            np.testing.assert_array_almost_equal(after_value, before_value)
	
