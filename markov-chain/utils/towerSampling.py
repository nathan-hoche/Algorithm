import random
from utils.node import node

class TowerSampling:
    def discret(graph, actual):
        link = graph[actual - 1].getLink()
        r = random.uniform(0, 1)

        s = 0.0
        pastID = 0
        for l in link:
            if (r < s):
                return l["id"]
            s += l["proba"]
            pastID = l["id"]
        return pastID
    
    def continuous(graph, actual):
        link = graph[actual - 1].getLink()
        r = random.uniform(0, 1)
        sProb = 0.0
        for l in link:
            sProb += l["proba"]
    
        s = 0.0
        pastID = 0
        for l in link:
            if (r < s):
                return l["id"]
            s += l["proba"]
            pastID = l["id"]
        return pastID