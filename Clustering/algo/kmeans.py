import time
import random
from PIL import Image

class algorithm():
    def __init__(self) -> None:
        self.pointList = []
        self.pointArray = []
        self.k = 5
        self.clusterList = []
        self.img = None
        self.imgpx = None
        self.time = -1
    
    def setup(self, pointArray: list[list[int, int, int]]=None, img:Image=None, imgpx=None) -> None:
        if (pointArray != None):
            self.img = img
            self.imgpx = imgpx
            self.pointArray = pointArray
            for i in pointArray:
                for j in i:
                    self.pointList.append(j)
  
    def addPoint(self, pt:list[int, int, int], cluster:int) -> None:
        self.clusterList[cluster]["count"] += 1
        self.clusterList[cluster]["points"].append(pt)
        for i in range(3):
            self.clusterList[cluster]["total"][i] += pt[i]
        total = self.clusterList[cluster]["total"]
        count = self.clusterList[cluster]["count"]
        self.clusterList[cluster]["center"] = [int(total[0] / count), int(total[1] / count), int(total[2] / count)]
    
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()

            ptList = self.pointList.copy()
            clusterFind = []
            for i in range(self.k):
                pt = random.choice(ptList)
                ptList.remove(pt)
                clusterFind.append(i)
                self.clusterList.append({"points": [pt], "center": pt, "total": pt, "count": 1})
            while(len(ptList) > 0):
                pt = ptList.pop(0)
                if (sum(pt) < 1000):
                    minIndex = 0
                    minValue = -1
                    for i in range(self.k):
                        dist = abs(sum(pt) - sum(self.clusterList[i]["center"]))
                        if (minValue == -1 or dist < minValue):
                            minValue = dist
                            minIndex = i
                    clusterFind.append(minIndex)
                    self.addPoint(pt, minIndex)
                else:
                    clusterFind.append(-1)

            self.time = time.time() - self.time

            lline = len(self.pointArray[0])
            for x in range(len(self.pointList)):
                if (clusterFind[x] != -1):
                    self.imgpx[x % lline, int(x / lline)] = tuple(self.clusterList[clusterFind[x]]["center"])
            self.img.save("img/result.png")

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            pass
            print("Cluster:")
            for i in range(self.k):
                print("Cluster", i, ":")
                print("\tValue:", self.clusterList[i]["center"])
                print("\tCount:", self.clusterList[i]["count"])
            print("Time: ", self.time)
