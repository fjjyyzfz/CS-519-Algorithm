from collections import defaultdict



def best(w, arr):
    opt = defaultdict(lambda: defaultdict(int))
    back = defaultdict(lambda: defaultdict(int))
    num_list = len(arr)

    def find_topdown(n, w):
        if n < 0 or (n in opt and w in opt[n]):
            return opt[n][w]
        k, v, c = arr[n]
        for j in range(c + 1):
            if k * j <= w:
                value = find(n - 1, w - k * j) + v * j
                if opt[n][w] < value:
                    opt[n][w] = value
                    back[n][w] = j
        return opt[n][w]
   
    def find_bottomup(w):    
        for w_i in range(1, w + 1):
            for j,(k, v, c) in enumerate(arr):
                for i in range(c + 1):
                    if k * i > w_i:
                        break
                    value = opt[j - 1][w_i - k * i] + v * i
                    if opt[j][w_i] < value:
                        opt[j][w_i] = value
                        back[j][w_i] = i
        return opt[num_list - 1][w]

    def backtrack(n, w):
        if n < 0:
            return []
        k, v, c = arr[n]
        return backtrack(n - 1, w - k * back[n][w]) + [back[n][w]]

    return find_bottomup(w), backtrack(num_list - 1, w)










if __name__ == "__main__":
    print(best(4, [(5, 5, 2)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))