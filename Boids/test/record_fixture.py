from Boids import boids
from Boids.boids import Boids
import os
__author__ = 'third'
import yaml
from copy import deepcopy

boids=Boids()
before = deepcopy(boids.boids)
boids.update_boids(boids.boids)
after = boids.boids
fixture = {"before": before, "after": after}
fixture_file = open(os.path.join(os.path.dirname(__file__),'fixtures','fixture.yml'), 'w')
fixture_file.write(yaml.dump(fixture))

fixture_file.close()
