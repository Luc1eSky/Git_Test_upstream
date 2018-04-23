import waypoint_loader
import tl_detector
import numpy as np


def wp_updater():
	
	base_waypoints = waypoint_loader.loader()

	multiplier = tl_detector.traffic()

	base_waypoints = np.array(base_waypoints) * multiplier

	return base_waypoints