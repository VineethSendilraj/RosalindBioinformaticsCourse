def rabbits_fibancci(months, offsprings):
    parents, child, newchild = 0, 1, 0
    for month in range(months - 1):
        if parents > 0:
            newchild = parents * offsprings

        if child > 0:
            parents += child
        child = newchild
    print(child + (parents))

rabbits_fibancci(31, 5)
