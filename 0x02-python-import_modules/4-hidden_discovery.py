#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    moduleList = dir()
    for x in range(0, len(moduleList)):
        if moduleList[x][:2] != "__":
            print(moduleList[x])
