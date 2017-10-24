# laboratory work #3 for Decision theory
# with class Container

import copy
from ContainerClass import Container

def max_container(containers):
    container_count = len(containers) - 1
    max_index = container_count
    max_weight = containers[container_count].getContainerWeight()
    for i in range(container_count - 1):
        if containers[i].getContainerWeight() > max_weight:
            max_weight = containers[i].getContainerWeight()
            max_index = i

    print "Max_weight: {}, {}".format(max_weight, max_index)
    return max_weight, max_index

document = open('1.txt', 'r')

container_capacity = 100
boxes = []
for number in document.readline().split():
    boxes.append(int(number))

print "DATA: {}".format(boxes)

# Next Fit Algorithm
containers = []
containers.append(Container())

for box in boxes:
    if containers[len(containers) - 1].getContainerWeight() + box <= container_capacity:
        containers[len(containers) - 1].add(box)
    else:
        containers.append(Container())
        containers[len(containers) - 1].add(box)

print "********"
print "Next Fit Algorithm:"
for container in containers:
    container.printContainer()

# First Fit Algorithm
containers = []
containers.append(Container())

for box in boxes:
    if containers[len(containers) - 1].getContainerWeight() \
            + box <= container_capacity:
        containers[len(containers) - 1].add(box)
    else:
        placed = False
        for i in range(len(containers) - 1):
            if containers[i].getContainerWeight() \
                    + box <= container_capacity:
                containers[i].add(box)
                placed = True
                break
        if not placed:
            containers.append(Container())
            containers[len(containers) - 1].add(box)

print "********"
print "First Fit Algorithm:"
for container in containers:
    container.printContainer()

# Worst Fit Algorithm
containers = []
containers.append(Container())

for box in boxes:
    if containers[len(containers) - 1].getContainerWeight() \
            + box <= container_capacity:
        containers[len(containers) - 1].add(box)
    else:
        min_weight = containers[len(containers) - 1].getContainerWeight()
        count = -1
        for i in range(0,len(containers) - 1):
            if containers[i].getContainerWeight() < min_weight:
                min_weight = containers[i].getContainerWeight()
                count = i
        # print min_weight
        if (min_weight + box) <= container_capacity:
            containers[count].add(box)
        else:
            containers.append(Container())
            containers[len(containers) - 1].add(box)


print "********"
print "Worst Fit Algorithm:"
for container in containers:
    container.printContainer()

# Best Fit Algorithm
containers = []
containers.append(Container())

for box in boxes:
    if containers[len(containers) - 1].getContainerWeight() \
            + box <= container_capacity:
        containers[len(containers) - 1].add(box)
    else:
        placed = False
        copy_containers = copy.deepcopy(containers)
        max_box = max_container(copy_containers)


