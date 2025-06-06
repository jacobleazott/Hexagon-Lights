# ╔════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦═══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦════╗
# ║  ╔═╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩═══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩═╗  ║
# ╠══╣                                                                                                             ╠══╣
# ║  ║    ANIMATIONS                               CREATED: 2022-09-02          https://github.com/jacobleazott    ║  ║
# ║══║                                                                                                             ║══║
# ║  ╚═╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦═══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦═╝  ║
# ╚════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩═══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩════╝
# ════════════════════════════════════════════════════ DESCRIPTION ════════════════════════════════════════════════════
# Collection of animations and patterns for the hexagon lights.
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
import board
import math
import neopixel
import numpy as np
import random

from coords import coordinates, polar_coordinates, gamma_table

pixel_pin = board.D18
num_pixels = 570
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.6, auto_write=False, pixel_order=ORDER
)

# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# MATH OPERATIONS ═════════════════════════════════════════════════════════════════════════════════════════════════════
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

def is_left_or_above(line_1, line_2, point):
    return ((line_2[0] - line_1[0]) * (point[1] - line_1[1]) - (line_2[1] - line_1[1]) * (point[0] - line_1[0])) > 0

def rotate_origin_only(xy, radians):
    x, y = xy
    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)

    return xx, yy

def find_distance(line1, line2, point1):
    l1 = np.array([line1[0], line1[1]])
    l2 = np.array([line2[0], line2[1]])
    p1 = np.array([point1[0], point1[1]])
    return abs(np.cross(l2 - l1, p1 - l1) / np.linalg.norm(l2 - l1))


# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# COLOR OPERATIONS ════════════════════════════════════════════════════════════════════════════════════════════════════
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

def hue_to_rgb(hue_value):
    x = int(255 * (1 - abs(((hue_value / 60) % 2) - 1)))
    if hue_value < 60:
        value = (255, x, 0)
    elif hue_value < 120:
        value = (x, 255, 0)
    elif hue_value < 180:
        value = (0, 255, x)
    elif hue_value < 240:
        value = (0, x, 255)
    elif hue_value < 300:
        value = (x, 0, 255)
    else:
        value = (255, 0, x)
    return value

def gen_random_color():
    return hue_to_rgb(random.randrange(0, 360, 1))

def gamma(uncorrected_color):
    return gamma_table[uncorrected_color[0]], gamma_table[uncorrected_color[1]], gamma_table[uncorrected_color[2]]

# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# ANIMATIONS ══════════════════════════════════════════════════════════════════════════════════════════════════════════
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

def rotating_line():
    def line(line_1, line_2):
        for idx, point in enumerate(coordinates):
            d = find_distance(line_1, line_2, point)
            if is_left_or_above(line_1, line_2, point):
                pixels[idx] = (255, 0, 0)
                if d < 1:
                    if d == 0:
                        pixels[idx] = (255, 0, 255)
                    else:
                        pixels[idx] = (255, 0, min(int((1/d)*10), 255))
            else:
                pixels[idx] = (0, 0, 255)
                if d < 1:
                    if d == 0:
                        pixels[idx] = (255, 0, 255)
                    else:
                        pixels[idx] = (min(int((1 / d) * 10), 255), 0, 255)
    
    line_point_1 = (0, -5)
    line_point_2 = (0, 5)
    for angle in np.arange(0, 2 * np.pi, 0.5):
        line(rotate_origin_only(line_point_1, angle), rotate_origin_only(line_point_2, angle))
        pixels.show()


def comet():
    thickness = 0.2
    fade = 25

    def streak(line_x_coord, line_color):
        for idx, point in enumerate(coordinates):
            dist = abs(line_x_coord - point[1])
            dist_thick = dist - thickness
            if dist_thick <= 0:
                pixels[idx] = line_color
            elif thickness > dist_thick > 0:
                tmp = [x * ((thickness - dist_thick) / thickness) for x in pixels[idx]]
                pixels[idx] = tmp
            elif pixels[idx] != [0, 0, 0]:
                mult = random.randrange(0, fade, 1) / 255
                var = (mult * line_color[0], mult * line_color[1], mult * line_color[2])
                tmp = (max(0, pixels[idx][0] - var[0]), max(0, pixels[idx][1] - var[1]), max(0, pixels[idx][2] - var[2]))
                pixels[idx] = tmp
                
    color = gen_random_color()
    
    for line_x in np.arange(0, 5, 0.1):
        streak(line_x, color)
        pixels.show()
        
def spin_rainbow():
    for angle in range(0, 360, 2):
        for idx, point in enumerate(polar_coordinates):
            theta = (point[1] + angle) % 360
            pixels[idx] = gamma(hue_to_rgb(theta))
        pixels.show()

# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# MAIN ════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    while True:
        # rotating_line()
        # comet()
        spin_rainbow()

# FIN ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════