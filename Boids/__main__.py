__author__ = 'third'
from Boids.flock import Flock
from Boids.boids import Boids

def process():
    flock=Flock()
    boid=Boids(flock, flock.flock_positions(), flock.flock_velocities())
    boid.simulate(show=True)

if __name__ == "__main__":
    process()