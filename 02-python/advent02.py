#!/usr/bin/python
import sys
# given string like "2x4x9", return x, y, z coords
def parse(str):
    l = str.split('x')
    return int(l[0]), int(l[1]), int(l[2])

def twosmallest(l):
    s = sorted(l)
    return s[0], s[1]

class dim:
    def __init__(self, x=None, y=None, z=None, str=None):
        self.x = x
        self.y = y
        self.z = z
        if str != None:
            self.x, self.y, self.z = parse(str)
    # how much wrapping paper do we need?
    def wrapit(self):
        total = 2 * self.x * self.y
        total += 2 * self.x * self.z
        total += 2 * self.y * self.z
        a, b = twosmallest([self.x, self.y, self.z])
        total += a * b
        return total
    def putabowonit(self):
        total = self.x * self.y * self.z
        a, b = twosmallest([self.x, self.y, self.z])
        total += 2 * (a + b)
        return total


def main(fn = None):

    wrap = 0
    ribbon = 0
    for l in fn:
        p = dim(str=l)
        wrap += p.wrapit()
        ribbon += p.putabowonit()

    print("wrapping paper: {}\nribbon length: {}".format(wrap, ribbon))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        main(sys.stdin)
    else:
        main(sys.argv[1])

