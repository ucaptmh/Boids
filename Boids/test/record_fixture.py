from Boids import boids
from Boids.boids import Boids
from Boids.boids import new_flock
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

flock_size = 50

positions=new_flock(flock_size, np.array([min_x_position,min_y_position]), np.array([max_x_position,max_y_position]))
velocities=new_flock(flock_size, np.array([min_x_velocity,min_y_velocity]), np.array([max_x_velocity,max_y_velocity]))
boids_test = Boids(positions,velocities)
before = deepcopy(boids_test.boids)
boids_test.update_boids(boids_test.positions,boids_test.velocities)
after = boids_test.boids
fixture = {"before": before, "after": after}
fixture_file = open(os.path.join(os.path.dirname(__file__),'fixtures','fixture.yml'), 'w')
fixture_file.write(yaml.dump(fixture))

fixture_file.close()
