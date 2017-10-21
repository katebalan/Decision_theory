# laboratory work #3 for Decision theory
# with class Container

import Container

document = open('1.txt', 'r')

boxes = []
for number in document.readline().split():
    boxes.append(number)

print "DATA: {}".format(boxes)

