import copy
import time
import heapq
import random




initial_state=[[3,2,1],[4,5,6],[8,7,0]]  # Initial state with 0 as blank space
final_state=[[1,2,3],[4,5,6],[7,8,0]] # target state with 0 as blank space




def checkValidPath(i,j):   # check if we are not going out of the index
    if i<3 and i>=0 and j<3 and j>=0:
        return True
    else:
        return False

def createChild(state,i,j,moves): # returns child nodes for a given state and position of blank space
    # i an j is the location of blank space("0")
    childrens=[]

    for move in moves:  # iterate over all the  possible move in moves list.
        if checkValidPath(i+move[0],j+move[1]):
            temp_state=copy.deepcopy(state)
            temp_state[i][j],temp_state[i+move[0]][j+move[1]]=temp_state[i+move[0]][j+move[1]],temp_state[i][j]
            childrens.append(temp_state)
    return childrens

def ManhattanDistance(state,include_blank=False):
    distance=0
    for i in range(3):
        for j in range(3):
            if state[i][j] !=0 or include_blank :
                for x in range(3):
                    for y in range(3):
                        if state[i][j]==final_state[x][y]:
                            distance+=abs(i-x)+abs(y-j)
    random_integer = random.randint(-30,30)
    return distance

def NoTilesDisplaced(state,include_blank=False):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=final_state[i][j] and ((state[i][j]!=0 and final_state[i][j]!=0) or include_blank):
                count+=1
    return count


def ManhattanDistanceWithrandomInt(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    if state[i][j] == final_state[x][y]:
                        distance += abs(i - x) + abs(y - j)
    random_integer = random.randint(-30, 30)
    return distance + random_integer


def Heuristics(state,type,include_blank=False):
    if type==1:
        return 0
    elif type==2:
        return NoTilesDisplaced(state,include_blank)
    elif type==3:
        return  ManhattanDistance(state,include_blank)
    elif type ==4 :
        return ManhattanDistanceWithrandomInt(state)
    else:
        print("No such Hurestic")



def getBlankPos(state): # Returns the location of blank space in the given state
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return [i,j]

def PrintHueristicType(heuristics_type):
    if heuristics_type==1:
        print("calculating for heuristics h(n)=0")
    elif heuristics_type==2:
        print("calculating for no of misplaced tiles")
    elif heuristics_type==3:
        print("calculating for manhatten distance")
    elif heuristics_type ==4 :
        print("calculating for manhatten distance with random int added")
    else:
        print("No such Hurestic")


def Astar(random_state,final_state,heuristics_type,include_blank=False): # DFS function
    visited = []  # List to store all the visited state
    heap = []  # data structure to be used for A star to store the state to be visited
    moves = [[-1,0], [1,0], [0, -1], [0,1]]  # possible moves
    heap.append([0+Heuristics(random_state,heuristics_type,include_blank),random_state,0]) # Insert Initial  cost,intial state, initial depth
    heapq.heapify(heap)

    while(len(heap)):
        cost,current_state,depth=heapq.heappop(heap) # visited node with least cost

        if final_state == current_state: # check if we have reached target state , If yes return depth
            return [depth,visited,heap]  ## returning depth of solution(depth), visited nodes(visited) and to be visited nodes(heap)
        visited.append(current_state) # add to the visited after visiting the node
        blanck_i,blanck_j=getBlankPos(current_state) # get the position of the blank space
        childerens = createChild(current_state, blanck_i, blanck_j,moves) # get a list of child node from current state which is not visted before
        for child in childerens:
            if child not in visited:
                heapq.heappush(heap,[Heuristics(child,heuristics_type,include_blank)+depth+1,child,depth+1]) # Add all the child node to visit in the stack after checking if we have visited it before





def RunAstar(initial_state,final_state,heuristics_type,include_blank=False):
    PrintHueristicType(heuristics_type)


    start = time.time()  # Inital timestamp
    result_depth, result_visited,result_tobe_visited = Astar(initial_state, final_state,heuristics_type,include_blank)

    end = time.time()
    print("number of node visited is :-", len(result_visited), " and target is found at a depth of :-", result_depth)
    print("Time taken in secs  to complete the code:- ", end - start)




def compareTwoHeuristic(heuristics_type_1,heuristics_type_2):

    #part of question 1 , 2 and 3
    print("H1 is :-")
    PrintHueristicType(heuristics_type_1)

    print("H2 is :-")
    PrintHueristicType(heuristics_type_2)



    output1_depth,output1_visited,output1_to_be_visted=Astar(initial_state, final_state, heuristics_type_1)

    print("Total node visited in H1 is", len(output1_visited))

    output2_depth,output2_vistied,output2_to_be_visted=Astar(initial_state, final_state, heuristics_type_2)
    #check if type2 is subset of type1
    print("total node visited in H2 is ", len(output2_vistied))


    print("States which are present in good Heuristics but not in bad Heuristics are:-")
    for i in range(min(len(output1_visited),len(output2_vistied))):
        if output2_vistied[i] not in output1_visited and output2_vistied[i] not in  [row[1] for row in output1_to_be_visted] :
            print(output2_vistied[i],i)




def checkMonotone(initial_state,final_state,heuristics_type,include_blank=False):
    PrintHueristicType(heuristics_type)

    visited = []  # List to store all the visited state
    heap = []  # data structure to be used for A star to store the state to be visited
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # possible moves
    heap.append([0 + Heuristics(initial_state, heuristics_type,include_blank), initial_state,0])  # Insert Initial  cost,intial state, initial depth
    heapq.heapify(heap)

    while (len(heap)):
        cost, current_state, depth = heapq.heappop(heap)  # visited node with least cost
        if final_state == current_state:  # check if we have reached target state , If yes return depth
            print("Monotonus Hurestics")
            return [depth, visited,heap]  ## returning depth of solution(depth), visited nodes(visited) and to be visited nodes(heap)
        visited.append(current_state)  # add to the visited after visiting the node
        blanck_i, blanck_j = getBlankPos(current_state)  # get the position of the blank space
        childerens = createChild(current_state, blanck_i, blanck_j,moves)  # get a list of child node from current state which is not visted before
        for child in childerens:
            if child not in visited:
                Hn = Heuristics(current_state, heuristics_type,include_blank)  ## calculating H(n)
                Hm=Heuristics(child, heuristics_type,include_blank)  ## calculating H(m)
                Cn=1 ## C(n,m) will always be 1 as cost from parent to child is always 1
                if Hn>Hm+Cn:
                    print("Given Heuristics is non Monotonus ")
                    print("Nth and Mth node for which H(n)>H(m)+C(n,m) is:-")
                    print("Nth node:-",current_state)
                    print("Mth node:-",child)
                    return

                heapq.heappush(heap, [Heuristics(child, heuristics_type,include_blank) + depth + 1, child,depth + 1])  # Add all the child node to visit in the stack after checking if we have visited it before




checkMonotone(initial_state,final_state,3,True)

















