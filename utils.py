
import math, pygame

def dist(r1, r2):
    "Find the distance between the center of two 'rectangles'"
    if type(r1) == pygame.Rect: x1, y1 = r1.center
    elif type (r1) == tuple: x1, y1 = r1
    else: x1, y1 = r1.rect.center # Assume it's a class with .rect. I.E. Unit

    if type(r2) == pygame.Rect: x2, y2 = r2.center
    elif type (r2) == tuple: x2, y2 = r2
    else: x2, y2 = r2.rect.center # Assume it's a class with .rect. I.E. Unit

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
