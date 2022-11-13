import os
import sys
import importlib
import json

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

def load_variable(filename: str) -> list[int]:
    try:
        with open("json/" + filename, "r") as f:
            data = json.load(f)
            print("Load: ", filename, "found.")
    except Exception as e:
        print("ERROR: File", filename, "not found.")
        print(e)
        exit(0)
    if type(data) == list:
        return data
    else:
        print("ERROR: Invalid type of variable.")
        exit(0)

######## Process Part ########

######## Main Part ########

def main():
    if len(sys.argv) != 3:
        print("ERROR: Invalid number of arguments.\n Usage: python3 tester.py [algo] [jsonfile]")
        return
    algo = load_algorithm(sys.argv[1])
    numberList = load_variable(sys.argv[2])
    algo.setup(numberList)
    algo.run()
    algo.print()

main()