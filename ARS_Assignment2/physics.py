from sensor import *
import visualization
import robotics


def collision_detection(robot, vel_right, vel_left, theta):
    if robot.sensor_num[0] < 55:
        if robot.y_init <= robot.y_pos:
            if robot.x_init > robot.x_pos:
                theta = np.pi
            else:
                theta = 0
    if robot.sensor_num[3] < 55:
        if robot.x_init <= robot.x_pos:
            if robot.y_init < robot.y_pos:
                theta = np.pi / 2
            else:
                theta = 3 * np.pi / 2
    if robot.sensor_num[6] < 55:
        if robot.y_init > robot.y_pos:
            theta = np.pi
    if robot.sensor_num[9] < 55:
        if robot.x_init > robot.x_pos:
            theta = np.pi / 2
    return vel_right, vel_left, theta

