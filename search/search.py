# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue
from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class Node:
    def __init__(self, state, parent, direction=None):
        self._state = state
        self._parent = parent
        self._direction = direction

    @property
    def state(self):
        return self._state

    @property
    def parent(self):
        return self._parent

    @property
    def direction(self):
        return self._direction

    def directPath(self):
        """

        :return: the path consists of directions:Direction
        """
        path = [self.direction]
        parent = self._parent
        while parent is not None and parent.direction is not None:
            path.insert(0, parent.direction)
            parent = parent.parent
        return path

    def nodesPath(self):
        """

        :return: the path consists of nodes
        """
        path = []
        parent = self._parent
        while parent is not None:
            path.insert(0, parent)
            parent = parent.parent
        return path

    @staticmethod
    def path_to_moves(nodePath):
        if len(nodePath) == 0:
            return None
        moves = []
        node1 = nodePath[0]
        for node2 in nodePath[1:]:
            moves.append(Node.get_direction(node1, node2))
            node1 = node2
        return moves

    str_direction_map = {
        'South': Directions.SOUTH,
        'North': Directions.NORTH,
        'East': Directions.EAST,
        'West': Directions.WEST
    }

    @staticmethod
    def get_direction(node1, node2):
        """
            Returns a direction from the state1 to the state2
        """

        if node2.state[0] - node1.state[0] == 1:
            return Directions.EAST
        elif node2.state[0] - node1.state[0] == -1:
            return Directions.WEST
        elif node2.state[1] - node1.state[1] == 1:
            return Directions.NORTH
        elif node2.state[1] - node1.state[1] == -1:
            return Directions.SOUTH

    def __str__(self):
        return "State: {0} - Path: " + self._path


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def graphSearch(problem, collection, pushMethod):
    """

    :rtype : []
    """
    bigO = 0

    fringe = collection
    pushMethod(fringe, Node(problem.getStartState(), None), None)

    closed = []

    while not fringe.isEmpty():
        node = fringe.pop()
        bigO += 1
        if problem.isGoalState(node.state):
            print 'BigO = ', bigO
            print 'Result = ', len(node.directPath())
            return node.directPath()
        if node.state not in closed:
            closed.append(node.state)
            for child in problem.getSuccessors(node.state):
                pushMethod(fringe, Node(child[0], node, child[1]), child[2])
    return None


def expand(node, problem):
    children = []
    for child in problem.getSuccessors(node.state):
        children.append(Node(child[0], node, child[1]))
    return children


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    return graphSearch(problem, Stack(),
                       lambda collection, node, weight: collection.push(node))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return graphSearch(problem, Queue(),
                       lambda collection, node, weight: collection.push(node))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return graphSearch(problem, PriorityQueue(),
                       lambda collection, node, weight: collection.push(node,
                                                                        weight))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
