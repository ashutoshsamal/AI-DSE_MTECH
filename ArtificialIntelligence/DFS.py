import copy
import time


start = time.time() # Inital timestamp

initial_state=[[3,2,1],[4,5,6],[8,7,0]]  # Initial state with 0 as blank space
final_state=[[1,2,3],[4,5,6],[7,8,0]] # target state with 0 as blank space


visited=[]  # List to store all the visited state
stack=[] # data structure to be used for DFS
max_depth=26 # maximum depth allowed for the DFS algo
moves=[[0,-1],[0,1],[1,0],[-1,0]] # possible moves

def checkValidePath(i,j):   # check if we are not going out of the index
    if i<3 and i>=0 and j<3 and j>=0:
        return True
    else:
        return False

def createChild(state,i,j): # returns child nodes for a given state and position of blank space
    # i an j is the location of blank space("0")
    childrens=[]

    for move in moves:  # iterate over all the  possible move in moves list.
        if checkValidePath(i+move[0],j+move[1]):
            temp_state=copy.deepcopy(state)
            temp_state[i][j],temp_state[i+move[0]][j+move[1]]=temp_state[i+move[0]][j+move[1]],temp_state[i][j]
            if temp_state not in visited:
                childrens.append(temp_state)
    return childrens


def getBlankPos(state): # Returns the location of blank space in the given state
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return [i,j]



def DFS(random_state,final_state): # DFS function

    stack.append([random_state,0]) # Insert Initial  state with initial depth 0

    while(len(stack)):
        current_state,depth=stack.pop() # visited the most recent node
        if depth<=max_depth and current_state not in visited:
            if final_state == current_state: # check if we have reached target state , If yes return depth
                return depth
            visited.append(current_state) # add to the visited after visiting the node
            blanck_i,blanck_j=getBlankPos(current_state) # get the position of the blank space
            childerens = createChild(current_state, blanck_i, blanck_j) # get a list of child node from current state which is not visted before
            for child in childerens:
                if child not in visited:
                    stack.append([child,depth+1]) # Add all the child node to visit in the stack after checking if we have visited it before


result_depth=DFS(initial_state,final_state) # Call the DFS function with initial and final state to get the depth at which we got the target state
end = time.time() # timestamp after th run is complete

print("number of node visited is :-",len(visited)," and target is found at a depth of :-" , result_depth) # print result

print("Time taken in secs  to complete the code:- ",end-start)









