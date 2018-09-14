
def best(w, arr):
    opt = {}
    back = {}
    num = [0] * len(arr)

    if w == 0:
        return

    def find(w):
        if w not in opt:
            opt[w] = 0
            back[w] = -1
        for i, (k, v) in enumerate(arr):
            if k <= w:
                value = find(w - k) + v
                if opt[w] < value:
                    opt[w] = value
                    back[w] = i
        return opt[w]


    def backtrack(w):
        if back[w] < 0:
            return
        k, v = arr[back[w]]
        backtrack(w - k)
        num[back[w]] += 1


    opt_val = find(w)
    backtrack(w)
    return opt_val, num

if __name__ == "__main__":
    print(best(3,[(2,4),(3,5)])) # output(5, [0, 1])
    print(best(3, [(1, 2), (1, 5)]))
    print(best(3, [(1, 2), (2, 5)]))
    print(best(92, [(8,9), (9,10), (10,12), (5,6)]))