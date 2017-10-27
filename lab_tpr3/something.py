# laboratory work #3 for Decision theory

from functions import *

train_document = open('1.txt', 'r')

boxes = []
for i in train_document:
    for box in i.split():
        boxes.append(int(box))

train_document.close()

print "*" * 15
print "DATA: {}".format(boxes)

container_capacity = 100

next_fit(boxes, container_capacity)
first_fit(boxes, container_capacity)
worst_fit(boxes, container_capacity)
best_fit(boxes, container_capacity)
print '---------------------'
print 'SORTED: '
next_fit(boxes, container_capacity, True)
first_fit(boxes, container_capacity, True)
worst_fit(boxes, container_capacity, True)
best_fit(boxes, container_capacity, True)
