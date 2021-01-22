import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getdict(self):
        d = {}
        d['col'] = self.x
        d['row'] = self.y
        return d


p = Point(10, 20)
print(json.dumps(p.__dict__))
print(json.dumps(p.getdict()))
