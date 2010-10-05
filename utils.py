
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

def calcAngle(p1, p2):
    """Calculate the angle between the line parellel to x that runs through p1
       and the line segment that connects p1 to p2"""
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.atan2(b, a)

