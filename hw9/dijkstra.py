from heapq import heappop, heappush
from collections import defaultdict

def generate_seq(k,length,seed): 
    import random; 
    random.seed(seed); 
    return [tuple(sorted(random.sample(range(k),2))+[random.randint(5,10)]) for _ in range(length)]
def shortest(n, graph):   
    def traceback(back, end):
        if back[end] == -1:
            return []
        return traceback(back, back[end]) + [back[end]]

    back = defaultdict(lambda : -1)
    way = defaultdict(list)
    for (u, v, weight) in graph:
        way[u].append((v, weight))
        way[v].append((u, weight))
    heap = []
    heappush(heap, (0, -1, 0))# shortestpath, prev, current
    visited = set()
    while(heap):
        short, prev, u = heappop(heap)
        if u not in visited:
            visited.add(u)
            back[u] = prev
            if u == n - 1:
                return short, traceback(back, n - 1) + [n - 1]
            for (v, weight) in way[u]:
                if v not in visited:
                    heappush(heap, (short + weight, u, v))

if __name__ == "__main__":
    dense_tuples = generate_seq(1000, 50000, 1)
    tuples_1 = generate_seq(5000, 50000, 1)
    tuples_2 = generate_seq(5000, 50000, 4)
    #print(tuples_1)
    print(shortest(1000, dense_tuples[:5000]))#25
    print(shortest(5000, tuples_1[:5000]))#111
    print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    # hp = heapdict()
    # hp[6] = 9
    # hp[1] = 4
    # v, k = hp.popitem()
    # print(k)