import copy

class Point():
    pass


blank = Point()


class Rectangle():
    pass


box = Rectangle()
box.w = 100.0
box.h = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(box):
    p = Point()
    p.x = box.corner.x + box.w / 2
    p.y = box.corner.y + box.h / 2
    # return (p.x,p.y)
    return p


# method for writing output
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


center = find_center(box)
print(center)
print_point(center)


# updating values
def grow_rect(box, dw, dh):
    box.w += dw
    box.h += dh
    return box


def print_updated(box):
    print('(%g, %g)' % (box.w, box.h))


grow_rect(box, 100, 200)
print_updated(box)
