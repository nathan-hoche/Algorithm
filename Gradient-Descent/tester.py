import os
import sys
import importlib

######## Loading Part ########

def load_algorithm(filename: str) -> object:
    try:
        sys.path.append(os.getcwd() + "/algo/")
        fd = importlib.import_module(filename.replace(".py", ""))
        print("Load: ", filename, "found.")
    except Exception as e:
        print("ERROR: File", filename, "not found.")
        print(e)
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

######## Setup Part ########

def getLambda(txt: str):
    with open("formula/" + txt, "r") as f:
        fr = f.read()
    return lambda x: eval(fr)

######## Main Part ########

def main():
    if len(sys.argv) != 3:
        print("ERROR: Invalid number of arguments.\n Usage: python3 tester.py [algo] [map]")
        return
    algo = load_algorithm(sys.argv[1])
    algo.setup(getLambda(sys.argv[2]))
    algo.run()
    algo.print()

main()