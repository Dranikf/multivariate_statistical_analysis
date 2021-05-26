import copy
from itertools import combinations



def two_combinator(objects, s1):

    result = []

    for obj1 in combinations(objects, s1):
        obj2 = list(set(objects) - set(obj1))
        result.append([list(obj1),obj2])

    return result



def ful_combinator(objects, sizes, appendics = []):

    result = []

    f = False

    for i in combinations(objects, sizes[0]):
        i = list(i)
        for_next = list(set(objects) - set(i))

        if f == False:
            appendics.append(i)
            f = True
        else:
            appendics[len(appendics) - 1] = i

        if len(sizes) != 1:
            for j in ful_combinator(for_next, sizes[1:], copy.copy(appendics)):
                j.insert(0,i)
                result.append(j)
        else:
            result.append([objects])

    
    return result
                

#test = ful_combinator([1,2,3,4,5,6,7,8,9,10,11,12], [4,4,4])

#f = open("result.txt", 'w')

#print(len(test))
#for i in test:
#    print(i)
#    f.write(str(i) + '\n')

#f.close()
