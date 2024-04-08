import copy
from collections import deque
import time

start = time.time() # Inital timestamp

initial_state=[[3,2,1],[4,5,6],[8,7,0]] # Initial state with 0 as blank space
final_state=[[1,2,3],[4,5,6],[7,8,0]] # target state with 0 as blank space

visited=[] # List to store all the visited state
q = deque()  # Queue is the data structure to be used for DFS

moves=[[0,-1],[0,1],[1,0],[-1,0]] # possible moves

def checkValidePath(i,j):
    if i<3 and i>=0 and j<3 and j>=0: # check if we are not going out of the index
        return True
    else:
        return False

def createChild(state,i,j): # returns child nodes for a given state and position of blank space
    # i an j is the location of blank space("0")
    childrens=[]

    for move in moves: # iterate over all the  possible move in moves list.
        if checkValidePath(i+move[0],j+move[1]):
            temp_state=copy.deepcopy(state)
            temp_state[i][j],temp_state[i+move[0]][j+move[1]]=temp_state[i+move[0]][j+move[1]],temp_state[i][j]
            if temp_state not in visited:
                childrens.append(temp_state)
    return childrens


def BFS(random_state,final_state): # DFS function
    q.append(random_state) # Initial state to be visited
    depth =0 # initial depth is 0
    if random_state ==final_state: # check if initial state is the target
        return depth
    else:
        visited.append(random_state) # mark initial state as visited

    while(len(q) and depth<50):
        l=len(q)
        depth+=1 # Increase depth by one as we are visiting the child of the previous state

        for _ in range(l): # Iterate l times to visit all the nodes from current depth
            current_state =q.popleft() # visit the node
            for i in range(len(current_state)):
                for j in range(len(current_state[0])):
                    if current_state[i][j] == 0:
                        childerens = createChild(current_state, i, j)  # Find the position of blank space and get the child to be visited .
            # visit the child node of all the visited states in previous depth level
            for child in childerens:
                if child not in visited:
                    print(child,depth)  # Print the state/node currently being visited
                    if child==final_state: # Return if we have reached the final state
                        return depth
                    else:
                        visited.append(child) # Add to the visited list
                        q.append(child) # Add to the queue , Child of these nodes will be visited in the next depth level.

result_depth=BFS(initial_state,final_state)

end = time.time() # timestamp after th run is complete

print("number of node visited is :-",len(visited)," and target is found at a depth of :-" , result_depth) # print result
print("Time taken in secs  to complete the code:- ",end-start)









