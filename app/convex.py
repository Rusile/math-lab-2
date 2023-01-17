import numpy as np


def cross_product(a):
    x1 = (a[1][0] - a[0][0])
    y1 = (a[1][1] - a[0][1])
    x2 = (a[2][0] - a[0][0])
    y2 = (a[2][1] - a[0][1])

    return x1 * y2 - y1 * x2


# Function to check if the polygon is convex polygon or not
def validate_convex(points):
    removed = []
    prev = 0
    i = 0

    while i < len(points):
        temp = [points[i], points[(i + 1) % len(points)], points[(i + 2) % len(points)]]
        curr = cross_product(temp)

        if curr == 0 or curr * prev < 0:
            removed.append(temp[1])
            points.remove(temp[1])
        else:
            prev = curr
            i += 1

    return removed


def cart2pol(point, center):
    rho = np.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)
    phi = np.arctan2(point[1] - center[1], point[0] - center[0])
    return rho, phi


def pol2cart(point, center):
    x = point[0] * np.cos(point[1]) + center[0]
    y = point[0] * np.sin(point[1]) + center[1]
    return round(x, 3), round(y, 3)


def make_convex(points: list):
    center = np.mean(points, axis=0)

    convex_pol = sorted(
        map(lambda point: cart2pol(point, center), points),
        key=lambda p: p[1],
        reverse=True
    )

    return list(map(lambda point: pol2cart(point, center), convex_pol))