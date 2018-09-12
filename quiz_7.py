# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by *** and Eric Martin for COMP9021


from math import pi, hypot


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'


class Disk:
    """
    >>> disk_1 = Disk()
    >>> disk_1
    Disk(Point(0.00, 0.00), 0.00)
    >>> disk_1.area
    0.0
    >>> disk_2 = Disk(Point(3, 0), 4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: __init__() takes 1 positional argument but 3 were given
    >>> disk_2 = Disk(centre = Point(3, 0), radius = 4)
    >>> disk_2.area
    50.26548245743669
    >>> disk_1.intersects(disk_2)
    True
    >>> disk_2.intersects(disk_1)
    True
    >>> Disk(centre = Point(0, 0), radius = 2).intersects(Disk(centre = Point(3, 4), radius = 3))
    True
    >>> disk_3 = disk_1.absorb(disk_2)
    >>> disk_3
    Disk(Point(3.00, 0.00), 4.00)
    >>> disk_1.change_radius(2)
    >>> disk_1.area
    12.566370614359172
    >>> disk_3 = disk_1.absorb(disk_2)
    >>> disk_1
    Disk(Point(0.00, 0.00), 2.00)
    >>> disk_2
    Disk(Point(3.00, 0.00), 4.00)
    >>> disk_3
    Disk(Point(2.50, 0.00), 4.50)
    >>> disk_4 = Disk(centre = Point(-4, 0), radius = 2)
    >>> disk_4.intersects(disk_1)
    True
    >>> disk_5 = disk_4.absorb(disk_1)
    >>> disk_5
    Disk(Point(-2.00, 0.00), 4.00)
    >>> disk_5.change_radius(5)
    >>> disk_5
    Disk(Point(-2.00, 0.00), 5.00)
    >>> disk_6 = Disk(centre = Point(1, 2), radius = 6)
    >>> disk_7 = disk_5.absorb(disk_6)
    >>> disk_7
    Disk(Point(-0.08, 1.28), 7.30)
    >>> disk_7.area
    167.54280759052244
    >>> disk_8 = Disk()
    >>> disk_8
    Disk(Point(0.00, 0.00), 0.00)
    >>> disk_8.change_radius(7)
    >>> disk_8.absorb(disk_7)
    Disk(Point(-0.05, 0.79), 7.79)
    """

    def __init__(self, *, centre=Point(0, 0), radius=0):
        self.__x = centre.x
        self.__y = centre.y
        self.__r = radius
        self.area = pi * radius ** 2

    def __repr__(self):
        return f'Disk(Point({self.__x:.2f}, {self.__y:.2f}), {self.__r:.2f})'

    def intersects(self, d):
        x2, y2 = d.get_x(), d.get_y()
        x1, y1 = self.__x, self.__y
        distance = hypot(x1 - x2, y1 - y2)
        if d.get_r() + self.__r < distance:
            return False
        else:
            return True

    def absorb(self, d):
        x2, y2 = d.get_x(), d.get_y()
        x1, y1 = self.__x, self.__y
        r1, r2 = self.__r, d.get_r()
        distance = hypot(x1 - x2, y1 - y2)

        if distance + min(r1, r2) > max(r1, r2):
            r3 = (distance + r1 + r2) / 2
            x3 = x1 + (x2 - x1) * (r3 - r1) / distance
            y3 = y1 + (y2 - y1) * (r3 - r1) / distance
            return Disk(centre=Point(x3, y3), radius=r3)
        elif r1 > r2:
            return Disk(centre=Point(self.__x, self.__y), radius=self.__r)
        else:
            return Disk(centre=Point(d.get_x(), d.get_y()), radius=d.get_r())

    def change_radius(self, r):
        self.__r = r
        self.area = pi * r * r

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_r(self):
        return self.__r


if __name__ == '__main__':
    import doctest

    doctest.testmod()
