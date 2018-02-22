import csv
import random
import math
import operator


def loadDataset(filename,split,trainingSet=[],testSet=[]):
    with open(filename,'rb') as csv:
        lines = csv.read(filename)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y]= float(dataset[x][y])
                if random.random < split:
                    trainingSet.append(dataset[x][y])
                else:
                    testSet(dataset[x][y])


def eculideanDistance(instance1, instance2,length):
    distance=0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]),2)
        return math.sqrt(distance)

