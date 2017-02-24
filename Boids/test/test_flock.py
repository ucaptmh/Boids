__author__ = 'third'
from Boids.flock import Flock
import numpy as np
from mock import Mock, patch
def test_flock_init():
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

    np.testing.assert_equal(flock.flock_size, 2)
    np.testing.assert_equal(flock.formation_flying_distance_sq,10000)

def test_flock_new_flock():
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
    rand=[1,2,3]
    with patch.object(np.random, 'rand', return_value=rand) as mock_method:
        test_flock=flock.new_flock(np.array([-450, 300]),np.array([50, 600]))
        np.testing.assert_array_almost_equal(test_flock, [[50,  550, 1050],[600,900, 1200]])

def test_flock_positions():
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
        rand=[1,2,3]
        with patch.object(np.random, 'rand', return_value=rand) as mock_method:
            test_flock=flock.flock_positions()
            np.testing.assert_array_almost_equal(test_flock, [[50,  550, 1050],[600,900, 1200]])

def test_flock_velocities():
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
        rand=[1,2,3]
        with patch.object(np.random, 'rand', return_value=rand) as mock_method:
            test_flock=flock.flock_velocities()
            np.testing.assert_array_almost_equal(test_flock, [[ 10,  20,  30],[ 20,  60, 100]])
