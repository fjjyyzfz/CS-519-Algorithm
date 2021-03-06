from collections import defaultdict

def order(n, edges):

    degrees = defaultdict(lambda : 1) # dummy source -> all v
    for u in edges:
        for v in edges[u]:
            degrees[v] += 1
    edges[-1] = range(n) # dummy source -> everybody
    print(edges)
    current = [-1] # zero-degrees nodes
    front = 0  # queue head pointer
    out = [] # final output order
    while front < len(current):
        v = current[front]
        out.append(v)
        front += 1 # pop queue head
        for u in edges[v]:
            degrees[u] -= 1
            if degrees[u] == 0:
                current.append(u)
            print(current)
    if len(out) == n+1:
        return out[1:] # excluding dummy source
    return None # cycle found

def longest(n, _edges):

    def solution(v):
        if v not in back: # doesn't need to start with 0
            return [v]
        return solution(back[v]) + [v]

    edges = defaultdict(list)
    for (u,v) in _edges:
        edges[u].append(v)
        
    topol = order(n, edges)
    for u in edges:
        edges[u].append(-1) # dummy sink (all v -> sink)
    best = defaultdict(int)
    print(best)
    back = {}
    for u in topol:
        for v in edges[u]: # forward update
            if best[u] + 1 > best[v]: 
                best[v] = best[u] + 1
                back[v] = u
    return best[-1]-1, solution(back[-1])

print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
#print(longest(20000, [(4402, 18651), (2067, 8358), (3863, 16234), (14728, 15474), (6879, 12439), (3075, 15986), (928, 12773), (14180, 19904), (69, 14594), (7496, 8727), (3349, 19370), (1002, 10401), (731, 833), (301, 17741), (7097, 12491), (951, 13831), (7264, 17289), (14348, 16246), (7637, 18116), (7565, 11327), (7169, 15060), (704, 9495), (13637, 18233), (3276, 6091), (3961, 9712), (10901, 16410), (13831, 16636), (6220, 9940), (9311, 19253), (16363, 16557), (12889, 19300), (1131, 15736), (7954, 13247), (5669, 13576), (12029, 17983), (2833, 12278), (14383, 16660), (3536, 5364), (12886, 17070), (12141, 16046), (969, 15378), (1424, 10109), (18945, 19437), (5582, 12897), (5524, 16457), (403, 7436), (6537, 17682), (7607, 17967), (13253, 16835), (11266, 18933), (11576, 15044), (8823, 17956), (187, 19953), (12572, 16793), (4235, 16996), (6733, 18394), (1839, 13962), (11951, 15764), (18166, 18677), (6548, 16538), (13546, 15890), (11691, 13579), (51, 11340), (17644, 17698), (10850, 15012), (916, 19656), (5806, 7523), (18047, 19151), (3001, 5923), (8365, 18056), (1063, 2308), (546, 2727), (477, 14843), (8177, 9214), (3587, 8802), (6049, 11286), (2277, 9512), (5230, 5487), (8362, 17281), (5509, 8942), (9649, 14899), (10551, 16269), (3741, 15524), (774, 10223), (11250, 12666), (6161, 13792), (3563, 8467), (8305, 16715), (6851, 19845), (682, 14144), (585, 7385), (4799, 13019), (1157, 5250), (14603, 16590), (13980, 17848), (7228, 16927), (7313, 14773), (1005, 17167), (12940, 18869), (10526, 13968)]))