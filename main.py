from random import *


class Locomotive:
    def __init__(self, speed=10):
        self.speed = speed


class Wagon:

    def __init__(self, size=2, weight=123,volume=100):
        self.size = size
        self.weight = weight
        self.volume=volume

class Train:
    def __init__(self):
        self.locomotive = Locomotive()
        self.wagons = []
        for i in range(randint(1, 5)):
            self.wagons.append(Wagon())


class Station:
    def __init__(self, size):
        self.storage = []
        self.size = size
        for i in range(size):
            self.storage.append(None)


class Railway:
    def __init__(self, start_point, finish_point):
        self.start_point = start_point
        self.finish_point = finish_point
        self.weight = random.randint(1, 6)


# class Storage:
#    pass


class Goods:
    def __init__(self, weight, volume, type ):
        self.weight = weight
        self.volume = volume
        self.type = type

