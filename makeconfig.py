__author__ = 'third'
import yaml
import numpy as np
import os

file_to_write_to = 'config.yaml'

flock_size=50
formation_flying_distance=100
formation_flying_strength=0.125
alert_distance=10
attraction_strength=0.01
axes_min=-500
axes_max=1500
lower_position_limit=np.array([-450, 300])
upper_position_limit=np.array([50, 600])
lower_velocity_limit=np.array([0, -20])
upper_velocity_limit=np.array([10, 20])
frame_number=50,
frame_interval=50

configdata ={"flock_size": flock_size,
"formation_flying_distance":formation_flying_distance,
"formation_flying_strength":formation_flying_strength,
"alert_distance":alert_distance,
"attraction_strength":attraction_strength,
"axes_min": axes_min,
"axes_max": axes_max,
"lower_position_limit":lower_position_limit,
"upper_position_limit":upper_position_limit,
"lower_velocity_limit":lower_velocity_limit,
"upper_velocity_limit":upper_velocity_limit,
"frame_number":frame_number,
"frame_interval":frame_interval}

with open('config.yaml', 'w') as f:
  yaml.dump(configdata, f, default_flow_style=False)

print('Written to file ' + file_to_write_to)