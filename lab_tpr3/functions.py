# laboratory work #3 for Decision theory

# Next Fit Algorithm
def next_fit(boxes, container_capacity, sort = False):
    if sort:
        boxes = sorted(boxes, reverse=True)

    containers = [[]]
    containers_count = 0
    sum_container = 0
    comparison_count = 0

    for box in boxes:
        sum_container += int(box)
        comparison_count += 1
        if sum_container <= container_capacity:
            containers[containers_count].append(box)
        else:
            sum_container = int(box)
            containers.append([])
            containers_count += 1
            containers[containers_count].append(box)

    print "*" * 15
    print "NFA: {}".format(containers)
    print "Comparations: {}".format(comparison_count)
    print "Conteiners: {}".format(len(containers))

# First Fit Algorithm
def first_fit(boxes, container_capacity, sort = False):
    if sort:
        boxes = sorted(boxes, reverse=True)

    containers = [[]]
    containers_count = 0
    containers_weight = [0]
    comparison_count = 0

    for box in boxes:
        comparison_count += 1
        if (containers_weight[containers_count] + box) <= container_capacity:
            containers[containers_count].append(box)
            containers_weight[containers_count] += box
        else:
            placed = False
            for i in range(containers_count):
                comparison_count += 1
                if (containers_weight[i] + box) <= container_capacity:
                    containers[i].append(box)
                    containers_weight[i] += box
                    placed = True
                    break
            comparison_count += 1
            if not placed:
                containers.append([])
                containers_count += 1
                containers[containers_count].append(box)
                containers_weight.append(box)

    print "*" * 15
    print "FFA: {}".format(containers)
    print "Comparations: {}".format(comparison_count)
    print "Conteiners: {}".format(len(containers))

# Worst Fit Algorithm
def worst_fit(boxes, container_capacity, sort = False):
    if sort:
        boxes = sorted(boxes, reverse=True)

    containers = [[]]
    containers_count = 0
    containers_weight = [0]
    comparison_count = 0

    for box in boxes:
        comparison_count += 1
        if (containers_weight[containers_count] + box) <= container_capacity:
            containers[containers_count].append(box)
            containers_weight[containers_count] += box
        else:
            min_weight = min(containers_weight)
            comparison_count += len(containers_weight)
            min_index = containers_weight.index(min_weight)
            comparison_count += 1
            if (min_weight + box) <= container_capacity:
                containers[min_index].append(box)
                containers_weight[min_index] += box
            else:
                containers.append([])
                containers_count += 1
                containers[containers_count].append(box)
                containers_weight.append(box)

    print "*" * 15
    print "WFA: {}".format(containers)
    print "Comparations: {}".format(comparison_count)
    print "Conteiners: {}".format(len(containers))

# Best Fit Algorithm
def best_fit(boxes, container_capacity, sort = False):
    if sort:
        boxes = sorted(boxes, reverse=True)

    containers = [[]]
    containers_count = 0
    containers_weight = [0]
    comparison_count = 0

    for box in boxes:
        comparison_count += 1
        if (containers_weight[containers_count] + box) <= container_capacity:
            containers[containers_count].append(box)
            containers_weight[containers_count] += box
        else:
            best_fit = []
            for iter in range(containers_count):
                comparison_count += 1
                if containers_weight[iter] + box <= container_capacity:
                    best_fit.append(containers_weight[iter])
            comparison_count += 1
            if not best_fit:
                containers.append([])
                containers_count += 1
                containers[containers_count].append(box)
                containers_weight.append(box)
            else:
                max_weight = max(best_fit)
                comparison_count += len(best_fit)
                max_index = containers_weight.index(max_weight)

                containers[max_index].append(box)
                containers_weight[max_index] += box

    print "*" * 15
    print "BFA: {}".format(containers)
    print "Comparations: {}".format(comparison_count)
    print "Conteiners: {}".format(len(containers))
