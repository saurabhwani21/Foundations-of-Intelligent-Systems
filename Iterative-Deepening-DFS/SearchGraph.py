import sys


# SearchGraph.py
#
# Implementation of iterative deepening search for use in finding optimal routes
# between locations in a graph. In the graph to be searched, nodes have names
# (e.g. city names for a map).
#
# An undirected graph is passed in as a text file (first command line argument). 
#
# Usage: python SearchGraph.py graphFile startLocation endLocation
# 
# Author: Richard Zanibbi, RIT, Nov. 2011
# Author: Saurabh A. Wani, RIT, Sep. 2016


def read_graph(filename):
    """Read in edges of a graph represented one per line,
    using the format: srcStateName destStateName"""
    print("Loading graph: " + filename)
    edges = {}

    inFile = open(filename)
    for line in inFile:
        roadInfo = line.split()

        # Skip blank lines, read in contents from non-empty lines.
        if (len(roadInfo) > 0):
            srcCity = roadInfo[0]
            destCity = roadInfo[1]

            if srcCity in edges:
                edges[srcCity] = edges[srcCity] + [destCity]
            else:
                edges[srcCity] = [destCity]

            if destCity in edges:
                edges[destCity] = edges[destCity] + [srcCity]
            else:
                edges[destCity] = [srcCity]

    print("  done.\n")
    return edges


######################################
# Add functions for search, output
# etc. here
######################################

def IDDFS(source, destination, limit, edges, path):
    """
    Takes in the problem and returns the path between the source and the destination or "Fail!" if the path does not exist.
    :param source: The location from where the path is to be found out.
    :param destination: The location until where the path is to be found out.
    :param limit: The maximum depth the code can handle.
    :param edges: Dictionary containing the locations and their connections.
    :param path:  List for storing the path between the source and destination or the error message.
    :return: The path between the source and destination or the error message.
    """

    path.append(source)

    for x in range(0, limit, 1):

        # List to store the locations visited.
        visited = []

        flag = DLS(source, destination, x, edges, path, visited)
        print("Level: ",x)

        for x in range(0, len(visited), 1):
            print(visited[x])
        print()
        if (flag == True):
            path.reverse()
            return path

    return False


def DLS(source, destination, limit, edges, path, visited):
    """
    Performs depth limited search to find out if a path exists between two locations.
    :param source: The location from where the path is to be found out.
    :param destination: The location until where the path is to be found out.
    :param limit: The maximum depth the code can handle.
    :param edges: Dictionary containing the locations and their connections.
    :param path:  List for storing the path between the source and destination or the error message.
    :param visited: List to store the locations visited.
    :return: True if a path exists or false if it does not.
    """
    if source not in visited:
        visited.append(source)
    # Checks if the given source and the destination are the same.
    if (source == destination):
        return True

    # Checks if the depth limit has been reached.
    if (limit <= 0):
        return False

    # Checks the adjacent neighbours of the given source.
    for x in edges[source]:
        if (DLS(x, destination, limit - 1, edges, path, visited) == True):
            path.insert(len(path) - 1, x)
            return True

    return False


def printPath(path):
    """
    Print the path between the source and destination or the error message if the path does not exist.
    :param path: List containing the path between the locations.
    :return: None
    """""
    if path == False:
        print("Fail!")
    else:
        for x in range(0, len(path), 1):
            print(path[x])

    # TBD


#########################
# Main program
#########################
def main():
    if len(sys.argv) != 4:
        print('Usage: python SearchGraph.py graphFilename startNode goalNode')
        return
    else:
        # Create a dictionary (i.e. associative array, implemented as a hash
        # table) for edges in the map file, and define start and end states for
        # the search. Each dictionary entry key is a string for a location,
        # associated with a list of strings for the adjacent states (cities) in
        # the state space.
        edges = {}
        edges = read_graph(sys.argv[1])
        start = sys.argv[2]
        goal = sys.argv[3]

        # Comment out the following lines to hide the graph description.
        print("-- Adjacent Cities (Edge Dictionary Data) ------------------------")
        for location in edges.keys():
            s = '  ' + location + ':\n     '
            s = s + str(edges[location])
            print(s)

        if not start in edges.keys():
            print("Start location is not in the graph.")
        else:
            path = []
            print('')

            print('-- States Visited ----------------')
            path = IDDFS(start, goal, 30, edges, path)
            print('')  # program will need to show the search tree.
            print('')

            print('--  Solution for: ' + start + ' to ' + goal + '-------------------')
            printPath(path)
            print()  # program will need to provide solution path or indicate failure.
            print('')

            print('--  Solution for: (?cityA) to (?cityB) -------------------')
            print('TBD')  # program will need to provide solution path or indicate failure.
            print('')

            print('--  Solution for: (?cityC) to (?cityD) -------------------')
            print('TBD')  # program will need to provide solution path or indicate failure.
            print('')


# Execute the main program.
main()
