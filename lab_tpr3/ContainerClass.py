class Container:

    def __init__(self):
        self.container_weight = 0
        self.container = []

    def add(self, new_container):
        self.container_weight += new_container
        self.container.append(new_container)

    def getContainerWeight(self):
        return self.container_weight

    def setContainerWeightToNull(self):
        self.container_weight = 0

    def printContainer(self):
        print "Container({}): {}".format(self.container_weight, self.container)
