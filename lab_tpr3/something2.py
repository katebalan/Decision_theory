# laboratory work #3 for Decision theory
# with class Container

from ContainerClass import Container

document = open('1.txt', 'r')

boxes = []
for number in document.readline().split():
    boxes.append(int(number))

print "DATA: {}".format(boxes)

containers = []
containers.append(Container())
container_capacity = 100

# Next Fit Algorithm
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
