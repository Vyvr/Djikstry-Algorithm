class Node:
    def __init__(self, id, is_visited, distance):
        self.id = id
        self.is_visited = is_visited
        self.distance = distance
        self.previous_node = None

    def __repr__(self):
        return repr(f'id: {self.id}, visited: {self.is_visited}, distance: {self.distance}, previous node: {self.previous_node}')
    
    def set_visited(self):
        self.is_visited = True