import re
import time
from os import listdir
from os.path import isfile, join
import subprocess as sb
import threading

programName = input("Tested program: ")
testRelPath = input("Test path: ")
path = "C:/Users/francik mateusz/Desktop/cpp/"
testPath = path + "tests/"
testDir = testPath + programName + testRelPath + "/in/"
answerDir = testPath + programName + testRelPath + "/out/"

testFiles = [f for f in listdir(testDir) if isfile(join(testDir, f))]
answerFiles = [f for f in listdir(answerDir) if isfile(join(answerDir, f))]


def timeout():
    print('timeout')
    exit(3)


def displayResults(num, file, received, expected, time):
    timeStr = "{:.4f}".format(time)
    if received != expected:
        print(f"{bcolors.FAIL}TEST #{num}: {file}, {timeStr}s{bcolors.ENDC}")
        print(f"\t Received: {received}")
        print(f"\t Expected: {expected}")
        return 0
    else:
        print(f"{bcolors.OKGREEN}TEST #{num}: {file}, {timeStr}s{bcolors.ENDC}")
        return 1


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


passed = 0
smallestSize = float('inf')
smallestFile = ""
for num in range(len(testFiles)):
    with open(testDir + testFiles[num]) as f:
        lines = f.read()
        t = threading.Timer(10, timeout)
        proc = sb.Popen(path + programName + ".exe", shell=True, stdin=sb.PIPE, stdout=sb.PIPE,
                        stderr=sb.PIPE, text=True)
        begin = time.time()
        out, err = proc.communicate(lines)
        end = time.time()
        t.cancel()
        with open(answerDir + answerFiles[num]) as f:
            passMod = displayResults(num, testFiles[num], out.strip(), f.read().strip(), end - begin)
            passed += passMod
            if passMod == 0:
                sizes = int(re.search(r'\d+', lines).group())
                if sizes < smallestSize:
                    smallestSize = sizes
                    smallestFile = testFiles[num]

print(f"{bcolors.OKCYAN}{passed} out of {len(testFiles)} passed{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Smallest file: {smallestFile} ({smallestSize}){bcolors.ENDC}")