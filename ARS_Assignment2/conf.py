import numpy as np

'MAIN'

WIDTH = 1280
HEIGHT = 720

'MOTION'

VEL_RIGHT = 1
VEL_LEFT = 1
SPEED = 0.5
T = 7
THETA = np.pi / 2
R = 30
# l = robot.r * 2
# R = (l / 2) * (vel_left + vel_right) / (vel_right - vel_left)
# w = (vel_right - vel_left) / l
# ICC_x = robot.x_pos - R * np.sin(theta)
# ICC_y = robot.y_pos + R * np.cos(theta)