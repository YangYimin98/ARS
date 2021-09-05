import pygame as p
import robotics
import sys


def initial_position(robot, width, height, r, screen, clock):
    flag = True
    distance = 25
    length = 10

    while flag:
        clock.tick(30)
        for event in p.event.get():
            if event.type == p.QUIT:
                flag = False
        k = p.key.get_pressed()
        if k[p.K_RIGHT]:
            robot.x_pos += length
        if robot.x_pos > width - (r + distance):
            robot.x_pos = width - (r + distance)
        if k[p.K_LEFT]:
            robot.x_pos -= length
        if robot.x_pos < r + distance:
            robot.x_pos = r + distance
        if k[p.K_UP]:
            robot.y_pos -= length
        if robot.y_pos < r + distance:
            robot.y_pos = r + distance
        if k[p.K_DOWN]:
            robot.y_pos += length
        if robot.y_pos > height - (r + distance):
            robot.y = height - (r + distance)
        if k[p.K_RETURN]:
            return True

        screen.fill((225, 225, 225))
        robotics.draw_boundary(width, height, screen)
        robotics.draw_robot(robot, screen)
        p.display.update()














