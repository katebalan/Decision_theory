class Container:
    container_weight = 0
    container = []

    def __init__(self, container):
        self.container_weight = container
        self.container.append(container)

    def add(self, new_container):
        self.container_weight += new_container
        self.container.append(new_container)

    def getContainerWeight(self):
        return self.container_weight

    def printContainer(self):
        print "Container({}): {}".format(self.container_weight, self.container)

containers = []
containers.append(Container(25))
containers[0].add(26)
containers[0].printContainer()
