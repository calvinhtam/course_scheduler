class GraphBuilder:

    def __init__(self, class_list=None, class_data=None):
        self.nodes = []
        self.al = {}

        self.add_nodes(class_list, class_data)
        self.create_adjacency_list()

    # read file for classes you need to build graph out
    def add_nodes(self, class_list, data):
        # chunk file, for each class in classList add_sections
        for name in class_list:
            # parse the department out
            dept_name = name.split()[0]
            print(dept_name)
            # this will be the courses
            course = data.departments[dept_name].courses[name]
            print(course.sections)
            for section in course.sections:
                for block in section.blocks:
                    # add to node list
                    pass
                pass
            pass

    def create_adjacency_list(self):
        # exhasutive, will be factorial time, will eventually need to find a way to make it better, like adding
        # all nodes as adjecency if it doesn't overlap in time&day, or final time&day
        # adjency list is made once per query, so maybe would be better to make giant hashtables of times so that lookup is constant even though building those tables
        # takes a shit ton of time
        pass

