import statistics as stats
import math 

class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def add_color(self, color):
        r = stats.mean([self.r, color.r])
        g = stats.mean([self.g, color.g])
        b = stats.mean([self.b, color.b])
        return Color(int(r), int(g), int(b))

if __name__=='__main__':
    blue = Color(0, 63, 76)
    red = Color(191, 84, 46)
    new_color = blue.add_color(red)
    print(new_color.r, new_color.g, new_color.b)