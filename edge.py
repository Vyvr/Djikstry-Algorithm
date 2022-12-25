class Edge:
	def __init__(self, start_node, end_node, distance):
		self.start_node = start_node
		self.end_node = end_node
		self.distance = distance

	def __repr__(self):
		return repr(f"start node: {self.start_node}, end node: {self.end_node}, weight: {self.distance}")
