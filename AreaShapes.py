class triangle:
    def __init__(self, base, height):
        self.b = int(base)
        self.h = int(height)
    def comp_area(self):
        ans = (1/2)*self.b*self.h
        return ans

class rectangle:
    def __init__(self, length, width):
        self.l = int(length)
        self.w = int(width)
    def comp_area(self):
        ans = self.l*self.w
        return ans

class square(rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class parallelogram(rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

class trapezoid:
    def __init__(self, a, b, height):
        self.a = int(a)
        self.b = int(b)
        self.h = int(height)
    def comp_area(self):
        ans = (1/2)*(self.a+self.b)*self.h
        return ans

class ellipse:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
    def comp_area(self):
        ans = 3.14*self.a*self.b
        return ans

class circle:
    def __init__(self, radius):
        self.r = int(radius)
    def comp_area(self):
        ans = (3.14)*(self.r**2)
        return ans

class sector:
    def __init__(self, radius, angle):
        self.r = int(radius)
        self.a = int(angle)
    def comp_area(self):
        ans = (1/2)*(self.r**2)*self.a
        return ans