# Boids
This programme produces a rudimentary simulation of basic flocking behaviour modelled on the famous Boids program my Craig Reynolds.

##Installation
To install run the following code:
* From command: `python setup.py install`
* Using pip: `pip install git+git://github.com/ucaptmh/Boids`
* Un-installation achieved by either a) deleting the relevant files or b) running `pip uninstall boids`

##Usage
Software may be ran from command line by simply running `Boids`
It has a number of optional parameters which may be implimented as follows:

`Boids [-h] [--file FILE] [--flock_size FLOCK_SIZE]
             [--flying_distance FLYING_DISTANCE]
             [--flying_strength FLYING_STRENGTH]
             [--alert_distance ALERT_DISTANCE]
             [--attraction_strength ATTRACTION_STRENGTH]`
* `FILE` : Optional YAML file to load parameters
* `FLOCK_SIZE` : Integer number of boids in the flock (default=50)
* `FLYING_DISTANCE` : Radius within which boids will try to match speed (default=100)
* `FLYING_STRENGTH` : How strongly boids will try to match speed (default=0.125)
* `ALERT_DISTANCE` : Radius within which boids will avoid each other (default=10)
* `ATTRACTION_STRENGTH` : How strongly boids will flock together (default=0.1)

Example: `Boids --flock_size 100 --attraction_strength 0.9`

This would produce a simulation with 100 boids an attraction strength of 0.9 and the other parameters set to default.

A python makeconfig file is provided, simply run this python script with desired parameters to create a config file to load into the `[--file FILE]` argument.

