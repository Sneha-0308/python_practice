class Water:
    def liquid(self):
        print("Liquid")


class Solid:
    def stone(self):
        print("Stone")


class Colloids(Water, Solid):
    def gels(self):
        print("Gel")


colloids = Colloids()
colloids.gels()
colloids.stone()
colloids.liquid()