import pygame as p
import physics
import motion
import robotics
from sensor import Sensor
import control
import sys
import conf


def main():
    screen = p.display.set_mode((conf.WIDTH, conf.HEIGHT))
    clock = p.time.Clock()
    flag = True
    r = conf.R
    vel_right = 1
    vel_left = 1
    speed = conf.SPEED
    t = conf.T
    theta = conf.THETA
    sensor = Sensor((conf.WIDTH // 2), (conf.HEIGHT // 2), r)
    robotics.draw_robot(sensor, screen)
    init = control.initial_position(
        sensor, conf.WIDTH, conf.HEIGHT, r, screen, clock)
    while flag:
        clock.tick(30)
        for event in p.event.get():
            if event.type == p.QUIT:
                flag = False
        k = p.key.get_pressed()
        if init:
            screen.fill((225, 225, 225))
            robotics.draw_boundary(conf.WIDTH, conf.HEIGHT, screen)
            x, y, theta = motion.draw_motion(
                sensor, vel_right, vel_left, t, theta, screen)
            vel_right, vel_left, theta = physics.collision_detection(
                sensor, vel_right, vel_left, theta)
        if k[p.K_w]:
            vel_left += speed
        if k[p.K_s]:
            vel_left -= speed
        if k[p.K_o]:
            vel_right += speed
        if k[p.K_l]:
            vel_right -= speed
        if k[p.K_x]:
            vel_left = vel_right = 0
        if k[p.K_t]:
            vel_left += speed
            vel_right += speed
        if k[p.K_g]:
            vel_left -= speed
            vel_right -= speed
        if k[p.K_0]:
            sys.exit()
        p.display.update()
