from node import *
import numpy as np
import csv
import pandas
from enum import IntEnum
import math


class Action(IntEnum):
    ADVANCE = 1
    U_TURN = 2
    TURN_RIGHT = 3
    TURN_LEFT = 4
    HALT = 5


class Maze:
    def __init__(self, filepath): # finished
        # TODO : read file and implement a data structure you like
        self.raw_data = pandas.read_csv(filepath).values
        self.nodes = []
        self.nd_dict = {}  # key: index, value: the correspond node
        for x in range(len(self.raw_data)):
            node = Node(self.raw_data[x][0])
            self.nodes.append(node)
            if x not in self.nd_dict.keys():
                self.nd_dict[x] = node
            for y in range(1,5):
                if not np.isnan(self.raw_data[x][y]):
                    node.setSuccessor(Node(self.raw_data[x][y]),y,self.raw_data[x][4+y])
        
    def getStartPoint(self):
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def getNodeDict(self):
        return self.nd_dict

    def BFS(self, nd):
        # TODO : design your data structure here for your algorithm
        # Tips : return a sequence of nodes from the node to the nearest unexplored deadend
        queue = []
        visited = []
        visited.append(nd)
        queue.append(nd)
        while queue:
            node = queue.pop(0)
            for n in node.Successors:
                if n[0] not in visited:
                    visited.append(n[0])
                    queue.append(n[0]) 
        return visited

    def BFS_2(self, nd_from, nd_to):
        # TODO : similar to BFS but fixed start point and end point
        # Tips : return a sequence of nodes of the shortest path
        cur_nd = nd_from
        visited = []
        visited.append(cur_nd)
        while cur_nd != nd_to:
            for n in cur_nd.Successors:
                if n[0] not in visited:
                            
        return visited

    def getAction(self, car_dir, nd_from, nd_to):
        # TODO : get the car action
        # Tips : return an action and the next direction of the car
        return None

    def strategy(self, nd):
        return self.BFS(nd)

    def strategy_2(self, nd_from, nd_to):
        return self.BFS_2(nd_from, nd_to)
