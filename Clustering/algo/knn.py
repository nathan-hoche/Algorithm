import time
import random
from PIL import Image

class algorithm():
    def __init__(self) -> None:
        self.pointList = []
        self.pointArray = []
        self.clusterList = []
        self.count = []
        self.img = None
        self.imgpx = None
        self.time = -1
    
    def setup(self, problem:dict=None, pointArray: list[list[int, int, int]]=None, img:Image=None, imgpx=None) -> None:
        if (problem != None and pointArray != None):
            self.clusterList = problem["ClusterWanted"]
            self.count = [0] * len(self.clusterList)
            self.img = img
            self.imgpx = imgpx
            self.pointArray = pointArray
            for i in pointArray:
                for j in i:
                    self.pointList.append(j)
    
    def findBestCluster(self, pt: list[int, int, int]) -> int:
        minIndex = 0
        minValue = -1
        for i in range(len(self.clusterList)):
            dist = 0
            for j in range(3):
                dist += abs(pt[j] - self.clusterList[i][j])
            if (minValue == -1 or dist < minValue):
                minValue = dist
                minIndex = i
        return minIndex
    
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()

            clusterFind = []
            ptList = self.pointList.copy()
            l = len(self.clusterList)
            while(len(ptList) > 0):
                pt = ptList.pop(0)
                if (sum(pt) < 1000):
                    minIndex = self.findBestCluster(pt)
                    clusterFind.append(minIndex)
                else:
                    clusterFind.append(-1)

            self.time = time.time() - self.time

            lline = len(self.pointArray[0])
            for x in range(len(self.pointList)):
                if (clusterFind[x] != -1):
                    self.count[clusterFind[x]] += 1
                    self.imgpx[x % lline, int(x / lline)] = tuple(self.clusterList[clusterFind[x]])
            self.img.save("img/result.png")

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            pass
            print("Cluster:")
            for i in range(len(self.clusterList)):
                print("Cluster", i, ":")
                print("\tValue:", self.clusterList[i])
                print("\tCount:", self.count[i])
            print("Time: ", self.time)
