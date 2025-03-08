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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    startState = (problem.getStartState(), [])
    stack.push(startState)
    actions = []
    visited = []
    current = stack.pop()
    while (problem.isGoalState(current[0]) == False):
        if (current[0] not in visited):
            successors = problem.getSuccessors(current[0])
            for s in successors:
                if(s[0] not in visited):
                    stack.push((s[0], actions + [s[1]]))
            visited = visited + [current[0]]
        current = stack.pop()
        actions = current [1]
    return actions
    util.raiseNotDefined()
    

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    startState = (problem.getStartState(), [])
    queue.push(startState)
    actions = []
    visited = []
    current = queue.pop()
    while (problem.isGoalState(current[0]) == False):
        if (current[0] not in visited):
            successors = problem.getSuccessors(current[0])
            for s in successors:
                if(s[0] not in visited):
                    queue.push((s[0], actions + [s[1]]))
            visited = visited + [current[0]]
            current = queue.pop()
            actions = current [1]
        else:
            current = queue.pop()
            actions = current[1]
    return actions
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    priorityQueue = util.PriorityQueue()
    startState = (problem.getStartState(), [])
    cost = problem.getCostOfActions(startState[1])
    priorityQueue.push((startState), cost)
    actions = []
    visited = []
    current = priorityQueue.pop()
 
    while (problem.isGoalState(current[0]) == False):
        if (current[0] not in visited):
            successors = problem.getSuccessors(current[0])
            for s in successors:
                costOf = problem.getCostOfActions(actions + [s[1]])
                if(s[0] not in visited):
                    priorityQueue.update((s[0], (actions + [s[1]])), costOf)
            visited = visited + [current[0]]
            current = priorityQueue.pop()
            actions = current [1]
        else:
            current = priorityQueue.pop()
            actions = current[1]
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priorityQueue = util.PriorityQueue()
    startState = (problem.getStartState(), [])
    startCost = problem.getCostOfActions(startState[1])
    startHeuristic = heuristic(startState[0], problem)
    totalCost = startCost + startHeuristic
    actions = []
    priorityQueue.push(startState, totalCost)
    visited = []
    current = priorityQueue.pop()
    
    while (problem.isGoalState(current[0]) == False):
        if (current[0] not in visited):
            successors = problem.getSuccessors(current[0])
            for s in successors:
                newCost = problem.getCostOfActions(actions + [s[1]])
                newHeuristic = heuristic(s[0], problem)
                newTotal = newCost + newHeuristic
                if(s[0] not in visited):
                    priorityQueue.update((s[0], (actions + [s[1]])), newTotal)
            visited += [current[0]]
            current = priorityQueue.pop()
            actions = current[1]
        else:
            current = priorityQueue.pop()
            actions = current[1]
    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
