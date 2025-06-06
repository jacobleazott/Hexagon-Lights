# ╔════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦═══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦════╗
# ║  ╔═╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩═══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩═╗  ║
# ╠══╣                                                                                                             ╠══╣
# ║  ║    GENERATE HEXAGON COORDINATES             CREATED: 2022-09-02          https://github.com/jacobleazott    ║  ║
# ║══║                                                                                                             ║══║
# ║  ╚═╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦═══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦═╝  ║
# ╚════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩═══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩════╝
# ════════════════════════════════════════════════════ DESCRIPTION ════════════════════════════════════════════════════
# Some crude code to plot out the hexagon configuration onto a plot and generate a list of coordinates.
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
import math
from math import sqrt
from matplotlib import pyplot as plt
import numpy as np

side = 2 / sqrt(3)
precision = 3
dx = 1
dy = (1 / sqrt(3))

left_seg = []
right_seg = []
top_left_seg = []
top_right_seg = []
down_left_seg = []
down_right_seg = []

for i in range(1, 20):
    # Vertical Segs
    left_seg.append((-1, -side / 2 + i * (side / 20)))
    right_seg.append((1, -side / 2 + i * (side / 20)))
    # Top Left/ Right Segs
    top_right_seg.append((i * (dx / 20), side - i * (dy / 20)))
    top_left_seg.append((-i * (dx / 20), side - i * (dy / 20)))
    # Bottom Left/ Right Segs
    down_left_seg.append((-1 + i * (dx / 20), -side / 2 - i * (dy / 20)))
    down_right_seg.append((1 - i * (dx / 20), -side / 2 - i * (dy / 20)))

hexs = []

test_hex = []

sets = []

set1, set2, set3, set4, set5, set6 = [], [], [], [], [], []

for point in left_seg:
    set1.append((point[0], point[1]))  # Self
    # test_hex.append((point[0] + 2, point[1]))              # Right
    set2.append((point[0] - 2, point[1]))  # Left
    set3.append((point[0] + 1, point[1] + sqrt(3)))  # Up Right
    set4.append((point[0] - 1, point[1] + sqrt(3)))  # Up Left
    set5.append((point[0] + 1, point[1] - sqrt(3)))  # Down Right
    set6.append((point[0] - 1, point[1] - sqrt(3)))  # Down Left

sets.append(set1)
sets.append(set2)
sets.append(set3)
sets.append(set4)
sets.append(set5)
sets.append(set6)
set1, set2, set3, set4, set5, set6 = [], [], [], [], [], []

for point in right_seg:
    set1.append((point[0], point[1]))  # Self
    set2.append((point[0] + 2, point[1]))  # Right
    # test_hex.append((point[0] - 2, point[1]))              # Left
    set3.append((point[0] + 1, point[1] + sqrt(3)))  # Up Right
    # test_hex.append((point[0] - 1, point[1] + sqrt(3)))    # Up Left
    set4.append((point[0] + 1, point[1] - sqrt(3)))  # Down Right
    # test_hex.append((point[0] - 1, point[1] - sqrt(3)))    # Down Left

sets.append(set1)
sets.append(set2)
sets.append(set3)
sets.append(set4)
set1, set2, set3, set4, set5, set6 = [], [], [], [], [], []

for point in top_left_seg:
    set1.append((point[0], point[1]))  # Self
    set2.append((point[0] + 2, point[1]))  # Right
    set3.append((point[0] - 2, point[1]))  # Left
    set4.append((point[0] + 1, point[1] + sqrt(3)))  # Up Right
    set5.append((point[0] - 1, point[1] + sqrt(3)))  # Up Left
    # test_hex.append((point[0] + 1, point[1] - sqrt(3)))    # Down Right
    set6.append((point[0] - 1, point[1] - sqrt(3)))  # Down Left

sets.append(set1)
sets.append(set2)
sets.append(set3)
sets.append(set4)
sets.append(set5)
sets.append(set6)
set1, set2, set3, set4, set5, set6 = [], [], [], [], [], []

for point in top_right_seg:
    set1.append((point[0], point[1]))  # Self
    set2.append((point[0] + 2, point[1]))  # Right
    set3.append((point[0] - 2, point[1]))  # Left
    set4.append((point[0] + 1, point[1] + sqrt(3)))  # Up Right
    set5.append((point[0] - 1, point[1] + sqrt(3)))  # Up Left
    set6.append((point[0] + 1, point[1] - sqrt(3)))  # Down Right
    # test_hex.append((point[0] - 1, point[1] - sqrt(3)))    # Down Left

sets.append(set1)
sets.append(set2)
sets.append(set3)
sets.append(set4)
sets.append(set5)
sets.append(set6)
set1, set2, set3, set4, set5, set6 = [], [], [], [], [], []

for point in down_left_seg:
    set1.append((point[0], point[1]))  # Self
    # test_hex.append((point[0] + 2, point[1]))              # Right
    set2.append((point[0] - 2, point[1]))  # Left
    # test_hex.append((point[0] + 1, point[1] + sqrt(3)))    # Up Right
    # test_hex.append((point[0] - 1, point[1] + sqrt(3)))    # Up Left
    set3.append((point[0] + 1, point[1] - sqrt(3)))  # Down Right
    set4.append((point[0] - 1, point[1] - sqrt(3)))  # Down Left

sets.append(set1)
sets.append(set2)
sets.append(set3)
sets.append(set4)
set1, set2, set3, set4, set5, set6 = [], [], [], [], [], []

for point in down_right_seg:
    set1.append((point[0], point[1]))  # Self
    set2.append((point[0] + 2, point[1]))  # Right
    # test_hex.append((point[0] - 2, point[1]))              # Left
    # test_hex.append((point[0] + 1, point[1] + sqrt(3)))    # Up Right
    # test_hex.append((point[0] - 1, point[1] + sqrt(3)))    # Up Left
    set3.append((point[0] + 1, point[1] - sqrt(3)))  # Down Right
    set4.append((point[0] - 1, point[1] - sqrt(3)))  # Down Left

sets.append(set1)
sets.append(set2)
sets.append(set3)
sets.append(set4)

hex_order = [25, 29, 10, 28, 8, 18, 9, 20, 14, 21, 15, 4, 13, 2, 24,
             6, 26, 30, 5, 23, 16, 1, 19, 11, 3, 17, 12, 7, 22, 27]
reverses = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 23, 24, 27, 28]

print(len(hex_order))

final_order = []
for x in hex_order:
    final_order.append(sets[x-1])

for x in reverses:
    final_order[x-1].reverse()

reduced_sigs = []
for seg in final_order:
    for point in seg:
        reduced_sigs.append((round(point[0], precision), round(point[1], precision)))

print(reduced_sigs)

polar_coords = []
polar_coords_deg = []

for seg in final_order:
    for point in seg:
        radius = math.sqrt(point[0]**2 + point[1]**2)
        theta = np.arctan2(point[1], point[0])
        deg = ((180 * theta/math.pi) + 360) % 360
        polar_coords.append((round(radius, precision), round(theta, precision)))
        polar_coords_deg.append((round(radius, precision), round(deg, precision)))

print(polar_coords)
print(polar_coords_deg)

plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()

plt.scatter(*zip(*left_seg))
plt.scatter(*zip(*top_left_seg))
plt.scatter(*zip(*top_right_seg))
plt.scatter(*zip(*right_seg))
plt.scatter(*zip(*down_right_seg))
plt.scatter(*zip(*reduced_sigs))

plt.show()


# FIN ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════