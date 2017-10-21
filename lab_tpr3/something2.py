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
print containers[0].printContainer()

for box in boxes:
    if containers[len(containers) - 1].getContainerWeight() + box <= container_capacity:
        pass