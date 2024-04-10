import random
import numpy as np
import copy


def checkValidPath(i,j):   # check if we are not going out of the index
    if i<3 and i>=0 and j<3 and j>=0:
        return True
    else:
        return False


def ManhattanDistance(state,final_state):
    distance=0
    for i in range(3):
        for j in range(3):
            if state[i][j] !=0 :
                for x in range(3):
                    for y in range(3):
                        if state[i][j]==final_state[x][y]:
                            distance+=abs(i-x)+abs(y-j)
    return distance

def NoTilesDisplaced(state,final_state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=final_state[i][j] and state[i][j]!=0:
                count+=1
    return count


def objectiveFunction(state,type,final_state):
    if type==1:
        return NoTilesDisplaced(state,final_state)
    elif type==2:
        return ManhattanDistance(state,final_state)
    else:
        print("No such Hurestic available")


def createChild(state,moves,cost_type,visited,final_state): # returns child nodes for a given state and position of blank space
    childrens=[]

    i,j=getBlankPos(state)  # i and j is the location of blank space("0")

    for move in moves:  # iterate over all the  possible move in moves list.
        if checkValidPath(i+move[0],j+move[1]):
            temp_state=copy.deepcopy(state)
            temp_state[i][j],temp_state[i+move[0]][j+move[1]]=temp_state[i+move[0]][j+move[1]],temp_state[i][j]
            if temp_state not in visited:
                childrens.append([temp_state,objectiveFunction(temp_state,cost_type,final_state)])
    return childrens

def getBlankPos(state): # Returns the location of blank space in the given state
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return [i,j]


def Randomize(state):
    temp=copy.deepcopy(state)
    for i in range(len(temp)):
        random.shuffle(temp[i])
    random.shuffle(temp)
    return temp



def HillClimbing(initialState,FinalState,cost_function_type,current_cost):
    current_state=copy.deepcopy(initialState)
    visited=[]
    goal_state=copy.deepcopy(FinalState)
    maxParallelWalk=200
    totalParallelwalk = 0
    current_state_cost=current_cost
    while (True):
        childeren = createChild(current_state, moves, cost_function_type, visited, goal_state)
        if len(childeren) == 0:
            break
        childeren.sort(key=lambda x: x[1])
        if current_state == goal_state:
            print("Reached solution with:-")
            print("number of state visited:-", len(visited))
            print("Path is:-")
            for route in visited:
                print(route)
                print("==>")
            condition = True
            return condition
        else:
            visited.append(current_state)
            best_neighbour = childeren[0][0]
            best_neighbour_cost = childeren[0][1]
            if current_state_cost > best_neighbour_cost:
                current_state = copy.deepcopy(best_neighbour)
                current_state_cost = best_neighbour_cost
            elif current_state_cost == best_neighbour_cost:
                totalParallelwalk += 1
                current_state = copy.deepcopy(best_neighbour)
                current_state_cost = best_neighbour_cost
                if totalParallelwalk > maxParallelWalk:
                    print("Stuck in a valley need to restart with another random initial state")
                    print("Total cost of the state is :-", current_state_cost)
                    print("total visited state is :-", len(visited))
                    break
            else:
                print("found a local minima")
                print("number of state visited:-", len(visited))
                print("Total cost of the state is :-", current_state_cost)
                break
    return False



a=[[6,7,3],[8,4,2],[1,0,5]]

b=[[1,2,3],[4,5,6],[7,8,0]]

moves = [[-1,0], [1,0], [0, -1], [0,1]]

condition=False
cost_function_type=1

for goal_state_restart in range(30):
    if condition:
        print("found the solution with number of goal state restart:-", goal_state_restart)
        break
    goal_state=Randomize(b)

    for intial_state_restart in range(100):
        if condition:
            print("found the solution with number of intial state  restart:-",intial_state_restart)
            break
        current_state = Randomize(a)
        current_state_cost = objectiveFunction(current_state, cost_function_type, goal_state)
        print("current State:-",current_state)
        print("Goal State:-",goal_state)
        condition=HillClimbing(current_state,goal_state,cost_function_type,current_state_cost)






















