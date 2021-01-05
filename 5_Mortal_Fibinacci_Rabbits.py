def rabbits_fibancci(months, lifeExpectancy):
    child, newChild, amount = 1, 0, 0
    finalParents = 0
    oldParents = []
    parents = []

    for month in range(months - 1):
        if len(oldParents) > 0:
            for item in oldParents:
                amount += item[0]
            newChild, amount = amount, 0 
            oldParents.clear()

        if len(parents) > 0:
            for item in parents:
                newChild += item[0]   #number of rabbits
                item[1] += 1   # increase Age
                if item[1] == lifeExpectancy: # if the age is max then remove it
                    oldParents.append(item)
        
            for pitem in oldParents:
                if (parents.count(pitem) > 0): # has the item in parents list
                    parents.remove(pitem)
        if child > 0:
            parents.append([child, 2]) 
        child, newChild = newChild, 0
        # print(month+2,"---->",oldParents, parents, child)
    
    if len(oldParents) > 0:
            for item in oldParents:
                finalParents += item[0]
    if len(parents) > 0:
            for item in parents:
                finalParents += item[0]
    
    print(child + finalParents)



rabbits_fibancci(95, 20)
