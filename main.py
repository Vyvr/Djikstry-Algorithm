from djikstry import Djikstry
from edge import Edge
from node import Node
import math

# Graph1
nodeA = Node('A', False, 0)
nodeB = Node('B', False, math.inf)
nodeC = Node('C', False, math.inf)
nodeD = Node('D', False, math.inf)
nodeE = Node('E', False, math.inf)
nodeF = Node('F', False, math.inf)
nodeG = Node('G', False, math.inf)

edge1 = Edge(nodeA, nodeB, 4)
edge2 = Edge(nodeA, nodeC, 3)
edge3 = Edge(nodeA, nodeE, 7)
edge4 = Edge(nodeB, nodeC, 6)
edge5 = Edge(nodeB, nodeD, 5)
edge6 = Edge(nodeC, nodeD, 11)
edge7 = Edge(nodeC, nodeE, 8)
edge8 = Edge(nodeD, nodeF, 2)
edge9 = Edge(nodeD, nodeG, 10)
edge10 = Edge(nodeE, nodeG, 5)
edge11 = Edge(nodeF, nodeG, 3)

node_list = [
    nodeA,
    nodeB,
    nodeC,
    nodeD,
    nodeE,
    nodeF, #end node
    nodeG,
    ]

edge_list = [
    edge1, 
    edge2,
    edge3,
    edge4,
    edge5,
    edge6,
    edge7,
    edge8,
    edge9,
    edge10,
    edge11,
    ]
djikstry_algorithm = Djikstry(edge_list, node_list, nodeF)

#####################
# Graph 2
# nodeA = Node('A', False, 0)
# nodeB = Node('B', False, math.inf)
# nodeC = Node('C', False, math.inf) #end node
# nodeD = Node('D', False, math.inf)
# nodeE = Node('E', False, math.inf)
# nodeF = Node('F', False, math.inf)

# edge1 = Edge(nodeA, nodeB, 2)
# edge2 = Edge(nodeA, nodeD, 8)
# edge3 = Edge(nodeB, nodeD, 5)
# edge4 = Edge(nodeB, nodeE, 6)
# edge5 = Edge(nodeD, nodeE, 3)
# edge6 = Edge(nodeD, nodeF, 2)
# edge7 = Edge(nodeE, nodeF, 1)
# edge8 = Edge(nodeE, nodeC, 9)
# edge9 = Edge(nodeF, nodeC, 3)

# node_list = [
#     nodeA,
#     nodeB,
#     nodeC,
#     nodeD,
#     nodeE,
#     nodeF,
#     ]

# edge_list = [
#     edge1, 
#     edge2,
#     edge3,
#     edge4,
#     edge5,
#     edge6,
#     edge7,
#     edge8,
#     edge9,
#     ]
# djikstry_algorithm = Djikstry(edge_list, node_list, nodeC)
################


djikstry_algorithm.get_shortest_path()