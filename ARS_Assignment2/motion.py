import robotics
import numpy as np


def rotation(robot, vel_right, vel_left):
    l = robot.r * 2
    R = (l / 2) * (vel_left + vel_right) / (vel_right - vel_left)
    w = (vel_right - vel_left) / l
    return l, R, w


def ICC(robot, vel_right, vel_left, theta):
    l, R, w = rotation(robot, vel_right, vel_left)
    ICC_x = robot.x_pos - R * np.sin(theta)
    ICC_y = robot.y_pos + R * np.cos(theta)
    return ICC_x, ICC_y


def draw_motion(robot, vel_right, vel_left, t, theta, screen):
    if vel_left == vel_right:
        theta = theta
        x_next = robot.x_pos + vel_left * np.cos(theta) * t
        y_next = robot.y_pos + vel_right * np.sin(theta) * t
    else:
        l, R, w = rotation(robot, vel_right, vel_left)
        ICC_x, ICC_y = ICC(robot, vel_right, vel_left, theta)
        x_next = np.cos(w * t) * (robot.x_pos - ICC_x) - \
            np.sin(w * t) * (robot.y_pos - ICC_y) + ICC_x
        y_next = np.sin(w * t) * (robot.x_pos - ICC_x) + \
            np.cos(w * t) * (robot.y_pos - ICC_y) + ICC_y
        theta = theta + w * t
    robot.x_init = robot.x_pos
    robot.y_init = robot.y_pos
    robot.x_pos = x_next
    robot.y_pos = y_next
    robotics.draw_robot(robot, screen)
    robot.draw_direction(screen, vel_right, vel_left, theta)
    return x_next, y_next, theta
