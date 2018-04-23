import numpy as np
import waypoint_loader

def traffic():
	
	base_waypoints = waypoint_loader.loader()

	# modify waypoints (change to mean) --> use np.array(base_waypoints).mean()
	multiplier = np.array(base_waypoints).mean()

	return multiplier