from collections import defaultdict

def order(nodes, edges):
    for i in range(nodes):
        edges.append((-1, i))
    #print(edges)  
    count = defaultdict(int)
    sortedlist = []
    for (a, b) in edges:
        if a not in count:
            count[a] = 0
        if b not in count:
            count[b] = 1
        else:
            count[b] += 1
    #print(count)
    i = 0
    cur = -1
    currentsort = [-1]
    while i < len(currentsort):
        sortedlist.append(currentsort[i])
        #print(sortedlist)
        cur = currentsort[i]
        #print(sortedlist)
        i += 1
        for (a, b) in edges:
            if a == cur:
                count[b] -= 1
                if count[b] == 0:
                    currentsort.append(b)

                    #print(currentsort)
    if len(sortedlist) != nodes + 1:
        return None
    else:
        return sortedlist[1:]





if __name__ == "__main__":
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
