from utils.node import node

class generateMarkovChain:

    def discret(k:int, t:int):
        # Create all nodes
        tabLink = []
        for n in range(1, k + 1):
            tabLink.append(node(n, -1))
        
        # Add link + proba
        directProba = 0.25
        for n in range(1, k + 1):
            # Horizontal
            if (n - 2 >= 0 and int((n - 1) / t) == int((n - 2) / t)):
                tabLink[n - 1].addLink(n - 1, tabLink[n - 2], directProba)
            if (int((n - 1) / t) == int((n) / t)):
                tabLink[n - 1].addLink(n + 1, tabLink[n], directProba)
            # Vertical
            if (n + t <= k):
                tabLink[n - 1].addLink(n + t, tabLink[n - 1 + t], directProba)
            if (n - t > 0):
                tabLink[n - 1].addLink(n - t, tabLink[n - 1 - t], directProba)
        return tabLink
    
    def continuous(rates:list = None, k:int=3):
        # Create all nodes
        tabLink = []
        for n in range(1, k + 1):
            tabLink.append(node(n, -1))
        
        # Add link + proba
        i = 0
        for n in range(1, k + 1):
            isEqual = -1
            for x in range(1, k):
                if (x == n):
                    isEqual += 1
                tabLink[n - 1].addLink(x + isEqual + 1, tabLink[x + isEqual], rates[i])
                i += 1
        return tabLink