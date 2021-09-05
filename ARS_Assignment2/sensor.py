import pygame as p
import numpy as np
from shapely.geometry import LineString
import conf


class Sensor(object):

    def __init__(self, x_pos, y_pos, r, color=(176, 224, 230)):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.sensor_num = [0] * 12
        self.r = r
        self.x_init = 0
        self.y_init = 0

    def draw_sensor(self, screen):

        black = (0, 0, 0)
        sensor = self.sensor_num
        v = self.sensor_num
        sensor_length = 25
        num = 0
        for i in range(0, 361, 30):
            if num <= 11:
                sensor[num] = p.draw.line(screen, black, (self.x_pos, self.y_pos),
                                          (self.x_pos + ((self.r + sensor_length) * np.sin(np.deg2rad(i))),
                                           self.y_pos + ((self.r + sensor_length) * np.cos(np.deg2rad(i)))), 2
                                          )
                x2 = self.x_pos + ((self.r + sensor_length) * np.sin(np.deg2rad(i)))
                y2 = self.y_pos + ((self.r + sensor_length) * np.cos(np.deg2rad(i)))

                line1 = LineString([(self.x_pos, self.y_pos), (x2, y2)])
                line2 = LineString([(sensor_length, sensor_length), (conf.WIDTH - sensor_length, sensor_length)])
                line3 = LineString([(sensor_length, sensor_length), (sensor_length, conf.HEIGHT - sensor_length)])
                line4 = LineString([(conf.WIDTH - sensor_length, sensor_length), (conf.WIDTH - sensor_length, conf.HEIGHT - sensor_length)])
                line5 = LineString([(conf.WIDTH - sensor_length, conf.HEIGHT - sensor_length), (sensor_length, conf.HEIGHT - sensor_length)])

                v[num] = sensor_length + self.r
                f2 = line1.intersection(line2)
                if line1.intersects(line2):
                    xy2 = f2.coords
                    for x, y in xy2:
                        v[num] = np.sqrt(np.power(x - self.x_pos, 2) + np.power(y - self.y_pos, 2))

                f3 = line1.intersection(line3)
                if line1.intersects(line3):
                    xy3 = f3.coords
                    for x, y in xy3:
                        v[num] = np.sqrt(np.power(x - self.x_pos, 2) + np.power(y - self.y_pos, 2))

                f4 = line1.intersection(line4)
                if line1.intersects(line4):
                    xy4 = f4.coords
                    for x, y in xy4:
                        v[num] = np.sqrt(np.power(x - self.x_pos, 2) + np.power(y - self.y_pos, 2))

                f5 = line1.intersection(line5)
                if line1.intersects(line5):
                    xy5 = f5.coords
                    for x, y in xy5:
                        v[num] = np.sqrt(np.power(x - self.x_pos, 2) + np.power(y - self.y_pos, 2))

                font = p.font.Font(None, 23)
                text_surface = font.render(str(int(round(v[num] - self.r))), True, black)
                if i >= 180:
                    screen.blit(text_surface,
                                (self.x_pos + ((self.r + sensor_length) * np.sin(np.deg2rad(i))),
                                 self.y_pos + ((self.r + sensor_length) * np.cos(np.deg2rad(i)))
                                 )
                                )
                else:
                    screen.blit(text_surface,
                                (self.x_pos + ((self.r + sensor_length - 15) * np.sin(np.deg2rad(i))),
                                 self.y_pos + ((self.r + sensor_length - 15) * np.cos(np.deg2rad(i)))
                                 )
                                )
                num += 1
        self.sensor_num = v
        return sensor

    def draw_direction(self, screen, vel_right, vel_left, theta):

        dark = (41, 36, 33)
        pos_x = self.x_pos + (self.r * np.cos(theta))
        pos_y = self.y_pos + (self.r * np.sin(theta))

        pos_x1 = self.x_pos - (self.r * np.cos(theta))
        pos_y1 = self.y_pos - (self.r * np.sin(theta))

        if vel_right < 0:
            if vel_left <= 0:
                p.draw.line(screen, dark, (self.x_pos, self.y_pos), (pos_x1, pos_y1), 2)
            else:
                p.draw.line(screen, dark, (self.x_pos, self.y_pos), (pos_x, pos_y), 2)

        else:
            if vel_left >= 0:
                p.draw.line(screen, dark, (self.x_pos, self.y_pos), (pos_x, pos_y), 2)
            else:
                p.draw.line(screen, dark, (self.x_pos, self.y_pos), (pos_x1, pos_y1), 2)
