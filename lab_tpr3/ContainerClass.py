class Container:

    def __init__(self):
        self.container_weight = 0
        self.container = []

    def add(self, new_container):
        self.container_weight += new_container
        self.container.append(new_container)

    def getContainerWeight(self):
        return self.container_weight

    def printContainer(self):
        print "Container({}): {}".format(self.container_weight, self.container)

def max_container(containers):
    container_count = len(containers) - 1
    max_weight = containers[container_count].getContainerWeight()
   for i in range(container_count - 1): -->FUCK FUCK
       pass