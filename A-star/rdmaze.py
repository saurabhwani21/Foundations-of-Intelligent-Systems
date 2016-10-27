# rdmaze.py
# Author: Vinay More, Ameya Nayak, Saurabh Wani, RIT, Oct.2016
import sys
import heapq
import math

def constructBoard():
    """constructBoard function constructs the board grid with nodes"""
    for i in range(0,Solution.rows):
        for j in range(0,Solution.columns):
            isWall=False
            if(i==0 or j==0 or i==Solution.rows-1 or j==Solution.columns-1):
                isWall=True
            #Node Assignment
            Solution.board[i][j]=Node(i,j,Solution.board[i][j],isWall)
            #Configuring Source Node
            if(Solution.board[i][j].value=='S'):
                Solution.source=Solution.board[i][j]
                Solution.source.dice['up']=1
                Solution.source.dice['below']=6
                Solution.source.dice['right']=3
                Solution.source.dice['left']=4
                Solution.source.dice['front']=2
                Solution.source.dice['back']=5
            #Configuring Goal Node
            if(Solution.board[i][j].value=='G'):
                Solution.goal=Solution.board[i][j]

def giveNeighbors(n):
    """giveNeighbors function returns all the valid neighbors for the node which has been passed"""
    #building neghbor list
    neighbor=[]
    if(n.i==0):
        if(n.j==0):
            neighbor.append(Solution.board[0][n.j+1])
            neighbor.append(Solution.board[n.i+1][0])
        elif(n.j==Solution.columns-1):
            neighbor.append(Solution.board[n.i+1][Solution.columns-1])
            neighbor.append(Solution.board[0][n.j-1])
        else:
            neighbor.append(Solution.board[n.i+1][n.j])
            neighbor.append(Solution.board[0][n.j-1])
            neighbor.append(Solution.board[0][n.j+1])
    elif(n.i==Solution.rows-1):
        if(n.j==0):
            neighbor.append(Solution.board[n.i-1][0])
            neighbor.append(Solution.board[Solution.rows-1][n.j+1])
        elif(n.j==Solution.columns-1):
            neighbor.append(Solution.board[n.i-1][Solution.columns-1])
            neighbor.append(Solution.board[Solution.rows-1][n.j-1])
        else:
            neighbor.append(Solution.board[n.i-1][n.j])
            neighbor.append(Solution.board[n.i][n.j-1])
            neighbor.append(Solution.board[n.i][n.j+1])
    else:
        if(n.j==0):
            neighbor.append(Solution.board[n.i+1][0])
            neighbor.append(Solution.board[n.i-1][0])
            neighbor.append(Solution.board[n.i][n.j+1])
        elif(n.j==Solution.columns-1):
            neighbor.append(Solution.board[n.i+1][n.j])
            neighbor.append(Solution.board[n.i-1][n.j])
            neighbor.append(Solution.board[n.i][n.j-1])
        else:
            neighbor.append(Solution.board[n.i+1][n.j])
            neighbor.append(Solution.board[n.i-1][n.j])
            neighbor.append(Solution.board[n.i][n.j-1])
            neighbor.append(Solution.board[n.i][n.j+1])
    return neighbor

def printBoardInitial():
    """printBoardInitial function prints the problem board grid"""
    for i in range(0,Solution.rows):
        for j in range(0,Solution.columns):
            print(str(Solution.board[i][j].value)+" ",end='')
        print("")

def printBoard(movei,movej):
    """printBoard function prints the updated board grid for current move which has been passed"""
    for i in range(0,Solution.rows):
        for j in range(0,Solution.columns):
            if(i==movei and j==movej):
                #printing current dice position in grid
                print("D ",end='')
            else:
                print(str(Solution.board[i][j].value)+" ",end='')
        print("")

def findpath(heuristicSelection):
    """findpath function is A* implementation with customized heuristics"""
    putCounter=0 #counter for nodes that are added in frontier
    getCounter=0 #counter for nodes that are removed from frontier

    #hcounter is used if there are two nodes in frontier queue with same f(n) and h(n) cost
    #then hcounter priortizes based on which was added first
    hcounter=0

    #visited is dictionary with key as the node and value is a list of dice states
    visited={}

    #frontier queue prioritizes based on f(n) cost then checks h(n)cost if f(n) cost was same
    #if both f(n) and h(n) values were same then the queue prioritizes based on hcounter
    frontier=MyQueue()
    frontier.put(Solution.source,0,0,0)
    putCounter=putCounter+1

    #Initial dice state at source is added
    visited[Solution.source]= [{'below': 6, 'up': 1, 'back': 5, 'front': 2, 'left': 4, 'right': 3}]

    while(not frontier.empty()):
        current=frontier.get()
        getCounter=getCounter+1
        if current.value==Solution.goal.value:
            break
        for n in giveNeighbors(current):
            if n.value=='*':
                continue
            else:
                n.currentCost = current.currentCost + 1
                currentCost = n.currentCost
                if(n.i>current.i):
                    if(current.dice['back']==6):
                        continue
                    current=moveFront(current)
                    n.dice=current.dice.copy()
                    current=moveBack(current)
                if(n.i<current.i):
                    if(current.dice['front']==6):
                        continue
                    current=moveBack(current)
                    n.dice=current.dice.copy()
                    current=moveFront(current)
                if(n.j>current.j):
                    if(current.dice['left']==6):
                        continue
                    current=moveRight(current)
                    n.dice=current.dice.copy()
                    current=moveLeft(current)
                if(n.j<current.j):
                    if(current.dice['right']==6):
                        continue
                    current=moveLeft(current)
                    n.dice=current.dice.copy()
                    current=moveRight(current)

                if(n.value=='G' and n.dice['up']!=1):
                    #Goal reached but up value not 1
                    continue

                #checking whether the current neghbor is the goal node with dice value at top as 1
                if(n.value=='G' and n.dice['up']==1):
                    print("No. of nodes put on the frontier: ",putCounter)
                    print("No. of nodes visited: ",getCounter)
                    return current.parent +"- " + str(current.i) + "," + str(current.j) + " - " + str(n.i) + "," + str(n.j)+" "

                #checking whether node was previously visited
                if(n in visited):
                    diceValues = visited[n].copy()
                    #If visited and dice orientation already exists, no point in adding it again
                    if n.dice in diceValues:
                        continue
                    else:
                        #if dice orientation is new at this visited node then add dice state.
                        visited[n].append(n.dice)
                else:
                    visited[n] = [n.dice]

                n.parent = current.parent + "- " + str(current.i) + "," + str(current.j)+" "
                if(heuristicSelection==1):
                    cost=currentCost+heuristic1(n,Solution.goal)
                elif(heuristicSelection==2):
                    cost=currentCost+heuristic2(n,Solution.goal)
                else:
                    cost=currentCost+heuristic3(n,Solution.goal)
                hcounter=hcounter+1

                #preparing node to be added at frontier
                tempNode=Node(n.i,n.j,Solution.board[n.i][n.j])
                tempNode.parent=n.parent
                tempNode.currentCost=n.currentCost
                tempNode.dice=n.dice.copy()
                putCounter=putCounter+1
                #Adding node on frontier. It takes node, f(n) i.e. cost, h(n) i.e. heuristic cost and hcounter
                if(heuristicSelection==1):
                    frontier.put(tempNode,cost,heuristic1(n,Solution.goal),hcounter)
                elif(heuristicSelection==2):
                    frontier.put(tempNode,cost,heuristic2(n,Solution.goal),hcounter)
                else:
                    frontier.put(tempNode,cost,heuristic3(n,Solution.goal),hcounter)

    print("No. of nodes put on the frontier: ",putCounter)
    print("No. of nodes visited: ",getCounter)
    return "No Solution"


def heuristic1(n,g):
    """heuristic1 function uses manhattan distance formula to compute cost"""
    return abs(g.i-n.i)+abs(g.j-n.j)

def heuristic2(n,g):
    """heuristic2 function uses Euclidean distance formula to compute cost"""
    return math.sqrt((g.i-n.i)*(g.i-n.i)+(g.j-n.j)*(g.j-n.j))

def heuristic3(n,g):
    """heuristic3 function returns the max of differences between x and y grid values"""
    return max(abs(g.i-n.i),abs(g.j-n.j))

def moveRight(s):
    """moveRight function updates the dice orientation by toppling it on right side"""
    left=s.dice['left']
    right=s.dice['right']
    up=s.dice['up']
    below=s.dice['below']
    s.dice['up']=left
    s.dice['below']=right
    s.dice['right']=up
    s.dice['left']=below
    return s

def moveLeft(s):
    """moveLeft function updates the dice orientation by toppling it on left side"""
    left=s.dice['left']
    right=s.dice['right']
    up=s.dice['up']
    below=s.dice['below']
    s.dice['up']=right
    s.dice['below']=left
    s.dice['right']=below
    s.dice['left']=up
    return s

def moveBack(s):
    """moveBack function updates the dice orientation by toppling it on back side"""
    front=s.dice['front']
    back=s.dice['back']
    up=s.dice['up']
    below=s.dice['below']
    s.dice['up']=front
    s.dice['below']=back
    s.dice['front']=below
    s.dice['back']=up
    return s

def moveFront(s):
    """moveFront function updates the dice orientation by toppling it on front side"""
    front=s.dice['front']
    back=s.dice['back']
    up=s.dice['up']
    below=s.dice['below']
    s.dice['up']=back
    s.dice['below']=front
    s.dice['front']=up
    s.dice['back']=below
    return s

#Main program
def main():
    """main function takes the puzzle file as input and then runs the A* algorithm to find solution by applying different heuristics"""
    if len(sys.argv) != 2:
        print('Usage: python rdmaze.py testFilename')
        return
    else:
        print("--------Rolling Die Mazes----------")
        lineCount=0
        #reading input file
        with open(sys.argv[1]) as file:
            for line in file:
                lineCount=lineCount+1
                Solution.board.append(list(line))
                columns=len(line)
            rows=lineCount
        Solution.rows=rows
        Solution.columns=columns

        #calling constructBoard function to transform it into maze of nodes
        constructBoard()
        print("Heuristic selection: ")
        print("Enter 1 for Manhattahn distance computation")
        print("Enter 2 for Euclidean distance computation")
        print("Enter 3 for computation based on maxmimum of x and y differences")
        heuristicSelection=int(input("Please enter 1 or 2 or 3: "))
        if(heuristicSelection==1 or heuristicSelection==2 or heuristicSelection==3):
            print("---------------------For heuristic "+str(heuristicSelection)+"--------------------------")
            printBoardInitial()
            a =findpath(heuristicSelection)
            expected=" - "+str(Solution.goal.i)+","+str(Solution.goal.j)
            if(expected in a):
                print("No. of moves in solution: "+str(a.count('-')-1))
                print(a)
                sol=Node(Solution.source.i,Solution.source.j)
                moveiprev=Solution.source.i
                movejprev=Solution.source.j
                pos=a.index('-',6)
                for itr in range(a.count('-')-1):
                    move=a[pos+2:a.index(' ',pos+2)]
                    movei=int(move[0:move.index(',')])
                    movej=int(move[move.index(',')+1:])
                    print("Next move:",str(movei)+","+str(movej))
                    printBoard(movei,movej)
                    if(movei>moveiprev):
                        sol=moveFront(sol)
                    elif(movei<moveiprev):
                        sol=moveBack(sol)
                    if(movej>movejprev):
                        sol=moveRight(sol)
                    elif(movej<movejprev):
                        sol=moveLeft(sol)
                    print(sol.dice)

                    if(pos<len(a)-8):
                        pos=a.index('-',pos+2)
                    moveiprev=movei
                    movejprev=movej
            else:
                print("No Solution")
        else:
            print("Wrong selection")

class MyQueue:
    """priority queue implementation with size, get, empty and put functions"""
    def __init__(self):
        self.queue = []
        self.itr = 0

    def size(self):
        #returns size of the queue
        return self.itr

    def get(self):
        #returns the first node from frontier queue's front.
        self.itr=self.itr-1
        return heapq.heappop(self.queue)[-1]

    def empty(self):
        #returns if queue is empty
        return self.itr==0

    def put(self, node, totalcost, heuristic, count):
        #adds node along with priority criteria
        #Here the queue is prioritized based on f(n) first then h(n) and then counter if there is a tie.
        heapq.heappush(self.queue, (totalcost, heuristic, count, self.itr, node))
        self.itr = self.itr + 1


class Node:
    """Node class represents every field on the grid"""
    i=0
    j=0
    value='.'
    isWall=False
    dice={}
    parent = ""
    currentCost = 0

    def __init__(self, i,j,val='.',isWall=False):
        """constructor to assign values while node creation"""
        self.i=i
        self.j=j
        self.value=val
        self.isWall=isWall
        self.dice['up']=1
        self.dice['below']=6
        self.dice['right']=3
        self.dice['left']=4
        self.dice['front']=2
        self.dice['back']=5

class Solution:
    """Solution class stores our board values"""
    board=[]
    source=0
    goal=0
    rows=0
    columns=0

main()
