from random import randint
import time

def findBestSubject(scores):
    indexBestSubject = 0
    x = 0
    for i in scores:
        if (i > scores[indexBestSubject]):
            indexBestSubject = x
        x += 1
    return indexBestSubject

class algorithm():
    def __init__(self) -> None:
        self.problem = {}
        self.time = -1
        self.firstGeneration = []
        self.actualGeneration = []
        self.scores = []
    
    def setup(self, problem: dict=None) -> None:
        if (problem != None):
            self.problem = problem
            for _ in range(0, self.problem["Preferences"]["NB_INDIVIDUALS"]):
                subject = {}
                for gene in self.problem["Genes"]["list"]:
                    subject[gene] = randint(self.problem["Genes"]["limit"]["min"], self.problem["Genes"]["limit"]["max"])
                self.firstGeneration.append(subject)
            self.actualGeneration = self.firstGeneration
    
    def fitness(self):
        self.scores = []
        for subject in self.actualGeneration:
            score = 0
            if (self.problem["FitnessFunction"] == "sum"):
                for mark in subject:
                    score += subject[mark]
            else:
                print("ERROR: FitnessFunction not found")
                exit(0)
            self.scores.append(score)
    
    def selection(self):
        classmentScore = self.scores.copy()
        classmentScore.sort(reverse=True)
        selectedSubject = []
        for x in range(0, self.problem["Preferences"]["NB_PARENT"]):
            selectedSubject.append(self.actualGeneration[self.scores.index(classmentScore[x])])
            self.scores.pop(self.scores.index(classmentScore[x]))
        self.actualGeneration = selectedSubject
    
    def croisement(self):
        subjectPostCroisement = []
        indexBestSubject = findBestSubject(self.scores)

        for subject in self.actualGeneration:
            crossoverIndex = randint(0, len(subject))
            listGene = self.problem["Genes"]["list"]
            
            # ADD First child
            i = 0
            genePart = {}
            while (i != crossoverIndex):
                genePart[listGene[i]] = subject[listGene[i]]
                i += 1
            while (i != len(subject)):
                genePart[listGene[i]] = self.actualGeneration[indexBestSubject][listGene[i]]
                i += 1
            subjectPostCroisement.append(genePart)
            i = 0

            # ADD Opposite child
            genePart = {}
            while (i != crossoverIndex):
                genePart[listGene[i]] = self.actualGeneration[indexBestSubject][listGene[i]]
                i += 1
            while (i != len(subject)):
                genePart[listGene[i]] = subject[listGene[i]]
                i += 1
            subjectPostCroisement.append(genePart)
        self.actualGeneration = subjectPostCroisement
        
    def mutation(self):
        mutation = self.problem["Genes"]["mutation"]
        for x in range(0, len(self.actualGeneration) - 1):
            module = self.problem["Genes"]["list"][randint(0, len(self.problem["Genes"]["list"]) - 1)]
            self.actualGeneration[x][module] = self.actualGeneration[x][module] + randint(mutation["min"], mutation["max"])
            if (self.actualGeneration[x][module] > self.problem["Genes"]["limit"]["max"]):
                self.actualGeneration[x][module] = self.problem["Genes"]["limit"]["max"]
            elif (self.actualGeneration[x][module] < self.problem["Genes"]["limit"]["min"]):
                self.actualGeneration[x][module] = self.problem["Genes"]["limit"]["min"]

    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()

            for _ in range(0, self.problem["Preferences"]["NB_GENERATIONS"]):
                self.fitness()
                self.selection()
                self.croisement()
                self.mutation()

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print("Objectif: " + self.problem["Objectif"])
            print("First Generation:", *self.firstGeneration, sep='\n')
            print("Final Generation:", *self.actualGeneration, sep='\n')
            print("Time: ", self.time)
