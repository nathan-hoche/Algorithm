
class node():
    def __init__(self, id, steadyState):
        self.Link = []
        self.id = id
        self.proba = steadyState
    
    def addLink(self, id, link, proba):
        self.Link.append({"id": id, "link": link, "proba": proba})
    
    def getProba(self, id):
        if (self.id == id):
            i = 1.0
            for x in self.Link:
                i = round(i - x["proba"], 4)
            return i
        for x in self.Link:
            if x["id"] == id:
                return x["proba"]
        return 0
    
    def getLink(self):
        return self.Link
    
    def sort(self):
        self.Link = sorted(self.Link, key=lambda k: k['proba'], reverse=True)

    def printLink(self):
        s = "Node " + str(self.id) + "("
        for x in self.Link:
            s += str(x["link"].id) + "->" + str(x["proba"]) + ", "
        s += ")"
        return s