import math

class Djikstry:
    def __init__(self, edge_list, node_list, end_node):
        self.start_node = None
        self.end_node = end_node
        self.node_list = node_list
        self.edge_list = edge_list
        self.visited_nodes = []
        self.unvisited_nodes = []

    def get_starting_node(self):
        for n in self.node_list:
            if n.distance == 0:
                n.set_visited()
                self.visited_nodes.append(n)
                starting_node = n
        
        for n in self.node_list:
            if n.is_visited == False:
                self.unvisited_nodes.append(n)
              
        return starting_node

    def set_node_visited(self, node):
        if node in self.visited_nodes: return
        self.visited_nodes.append(node)
        self.unvisited_nodes.remove(node)
        node.is_visited = True

    def get_adcjent_edges(self, node):
        adcjent_edges = []
        for e in self.edge_list:
            if e.start_node == node:
                adcjent_edges.append(e)
            if e.end_node == node:
                adcjent_edges.append(e)

        return adcjent_edges

    def get_adcjent_nodes(self, node):
        adcjent_nodes = []
        for e in self.edge_list:
            if e.start_node == node:
                adcjent_nodes.append(e.end_node)
            if e.end_node == node:
                adcjent_nodes.append(e.start_node)

        return adcjent_nodes

    def calculate_neighbours_distance(self, node):
        adcjent_edges = self.get_adcjent_edges(node)

        for a in adcjent_edges:
            #grab adcjent node
            if a in self.visited_nodes: continue
            adcjent_node = None
            if a.start_node != node:
                adcjent_node = a.start_node
            else:
                adcjent_node = a.end_node

            #check if distance sum is lower than his distance
            dist_sum = a.distance + node.distance

            if dist_sum < adcjent_node.distance:
                adcjent_node.distance = dist_sum
                adcjent_node.previous_node = node
    
    def get_node_with_lowest_distance(self, nodes):
        if len(nodes) == 0: return
        closest_node = nodes[0]
        counter = 1
        while counter < len(nodes):
            if closest_node.distance > nodes[counter].distance:
                closest_node = nodes[counter]
            counter += 1
        return closest_node
            
            
    def algorithm(self):
        node = self.get_starting_node()
        self.calculate_neighbours_distance(node)

        while len(self.unvisited_nodes) != 0:
            adcjent_nodes = self.get_adcjent_nodes(node)
            for an in adcjent_nodes:
                self.calculate_neighbours_distance(an)
            self.set_node_visited(node)
            node = self.get_node_with_lowest_distance(self.unvisited_nodes)
    
    def get_shortest_path(self):
        node = self.end_node
        path = []
        self.algorithm()

        while node != None:
            path.append(node.id)
            node = node.previous_node
        
        path.reverse()

        for node in path:
            print(node)
