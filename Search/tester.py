import os
import sys
import importlib

######## Loading Part ########

def load_algorithm(filename: str) -> object:
    try:
        sys.path.append(os.getcwd() + "/algo/")
        fd = importlib.import_module(filename.replace(".py", ""))
        print("Load: ", filename, "found.")
    except:
        print("ERROR: File", filename, "not found.")
        exit(0)
    try:
        classfd = fd.algorithm()
        print("Load: Class found. -> ", type(classfd))
        ####### Check if sample fonction is set
        classfd.setup()
        classfd.run(True)
        classfd.print(True)
        #######################################
    except Exception as e:
        print("ERROR: class/method crashed")
        print(e)
        exit(0)
    return classfd

######## Game Part ########

def getFormatedMap(mapName: str) -> list:
    with open("map/" + mapName, "r") as file:
        mapf = file.read()
    tmpStart = mapf.find('S')
    tmpEnd = mapf.find('E')
    mapf = mapf.replace('S', '0').replace('E', '0').replace('#', '1').replace('-', '0')
    mapl = mapf.split('\n')
    mapl = [list(mapl[i]) for i in range(len(mapl))]
    mapl = [[int(mapl[i][j]) for j in range(len(mapl[i]))] for i in range(len(mapl))]
    start = (int(tmpStart / (len(mapl[0]) + 1)), tmpStart % (len(mapl[0]) + 1))
    end = (int(tmpEnd / (len(mapl[0]) + 1)), tmpEnd % (len(mapl[0]) + 1))
    return mapl, start, end


def game(algo: object, mapName: str) -> None:
    mapl, start, end = getFormatedMap(mapName)
    algo.setup(mapl, start, end)
    algo.run()
    algo.print()

######## Main Part ########

def main():
    if len(sys.argv) != 3:
        print("ERROR: Invalid number of arguments.\n Usage: python3 tester.py [algo] [map]")
        return
    algo = load_algorithm(sys.argv[1])
    game(algo, sys.argv[2])

main()