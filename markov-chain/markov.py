import math
from utils.generation import generateMarkovChain
from utils.towerSampling import TowerSampling
import random

def getTransProb(i:int, j:int, k:int) -> float:
    t = int(math.sqrt(k))
    nodes = generateMarkovChain.discret(k, t)
    return nodes[i - 1].getProba(j)

def getSejProb(s1:int, s2:int, numStates:int, TS:int) -> float:
    t = int(math.sqrt(numStates))
    nodes = generateMarkovChain.discret(numStates, t)
    for node in nodes:
        node.sort()

    count = [0] * (numStates)
    i = s1 # need to be a random number ?
    for _ in range(0, 100000):
        i = s1 # Doit être ici?
        for _ in range(0, TS):
            i = TowerSampling.discret(nodes, i)
        count[i - 1] += 1
    res = count[s2 -1]
    globalr = 0
    for x in count:
        globalr += x
    return res / globalr

def getBiasTransProb(s1:int, s2:int, ssprob:list[float]) -> float:
    numStates = len(ssprob)
    t = int(math.sqrt(numStates))
    nodes = generateMarkovChain.discret(numStates, t)
    Paac = 0
    Sum = 0
    nodes[s1 - 1].printLink()
    Total_link = len(nodes[s1 - 1].getLink()) + 1
    if (s1 != s2):
        for x in nodes[s1 - 1].getLink():
            if (x["id"] == s2):
                Paac = min(1, ssprob[s2-1]/ssprob[s1-1])
                return Paac * (1 / Total_link)
        return 0.0
    if (Total_link == 5):
        return 0.0
    for x in nodes[s1 - 1].getLink():
        if (x["id"] != s1):
            Paac = min(1, ssprob[x["id"]-1]/ssprob[s1-1])
            Sum += Paac * (1 / Total_link)
    return 1 - Sum


def getContTransProb(s1:int, s2:int, rates:list[float]) -> float:
    nodes = generateMarkovChain.continuous(rates)
    Sum = 0
    for x in nodes[s1 - 1].getLink():
        Sum += x["proba"]
    return nodes[s1 - 1].getProba(s2) / Sum

def getContSejProb(s1:int, s2:int, rates:list[float], TSC:float) -> float:
    nodes = generateMarkovChain.continuous(rates, 3)
    for node in nodes:
        node.sort()
    count = [0] * (3)
    actual = s1
    for _ in range(0, 100000):
        T = 0
        while T < TSC:
            r = random.uniform(0, 1)
            P = 0
            for x in rates:
                P += x
            dt = (-1.0 / P) * math.log(r)
            T += dt
            actual = TowerSampling.continuous(nodes, actual)
        count[actual - 1] += 1
        actual = s1
    res = count[s2 -1]
    globalr = 0
    for x in count:
        globalr += x
    return res / globalr

print("A1:", getTransProb(1, 2, 9))
print("A2:", getTransProb(1, 1, 4))
print("A3:", getSejProb(1, 1, 9, 4))
print("A4:", getBiasTransProb(4, 4, [0.1,0.1,0.1,0.2,0.1,0.2,0.05,0.05,0.1]))
print("A5:", getContTransProb(1, 2, [10.0, 5.0, 1.0, 2.0, 5.0, 2.0]))
print("A6:", getContSejProb(1, 1, [10.0, 5.0, 1.0, 1.0, 2.0, 3.0], 0.02))