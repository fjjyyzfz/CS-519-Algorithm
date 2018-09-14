from collections import defaultdict

def lis(input):
    string = input + '}'
    str_int = list(map(lambda x:ord(x), string))
    back = defaultdict(lambda : -1)
    length = len(input)
    if length == 0:
        return 0
    def find(index, opt = defaultdict(int)):
        if index == 0:
            opt[index] = 1
        if index in opt:
            return opt[index]
        for i in range(index):
            if i == 0:
                opt[index] = 1
                back[index] = 0
            value = find(i) + 1
            if str_int[index] > str_int[i] and value > opt[index]:    
                opt[index] = value
                back[index] = i
        return opt[index]
    def traceback(index):
        if back[index] == -1:
            return ""
        return traceback(back[index]) + input[back[index]]
    a = find(length)
    return traceback(length)





if __name__ == "__main__":
    print(lis("aebbcg"))
    print(lis(""))
    print(lis("aubysx"))
    print(lis("zyx"))