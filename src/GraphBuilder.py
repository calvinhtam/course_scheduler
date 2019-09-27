class GraphBuilder:

    def __init__(self, classList):
        self.nodes = []
        self.al = {}

        self.add_nodes(classList)
        self.create_adjacency_list()
        pass

    # read file for classes you need to build graph out
    def add_nodes(self, class_list):
        # chunk file, for each class in classList add_sections
        pass

    # will add all sections of a course to the nodes
    def add_sections(self, course):
        pass

    def create_adjacency_list(self):
        pass

