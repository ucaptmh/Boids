from Boids import boids
from Boids.boids import Boids
from Boids.flock import Flock
import os
import numpy as np
__author__ = 'third'
import yaml

from copy import deepcopy

min_x_position, max_x_position = -450, 50
min_y_position, max_y_position = 300, 600
min_x_velocity, max_x_velocity = 0, 10
min_y_velocity, max_y_velocity = -20, 20

axes_min, axes_max = -500, 1500

flock=Flock()

positions=flock.new_flock(np.array([min_x_position,min_y_position]), np.array([max_x_position,max_y_position]))
velocities=flock.new_flock(np.array([min_x_velocity,min_y_velocity]), np.array([max_x_velocity,max_y_velocity]))
boids_test = Boids(flock,positions,velocities)
before = deepcopy(boids_test.boids)
boids_test.update_boids()
after = boids_test.boids
fixture = {"before": before, "after": after}
fixture_file = open(os.path.join(os.path.dirname(__file__),'fixtures','regression_fixture.yml'), 'w')
fixture_file.write(yaml.dump(fixture))

fixture_file.close()
