class Course:
    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.sections = []
        self.prereqs = set()

    def display(self):
        print("Name: {}, Units {}").format(self.name, self.units)