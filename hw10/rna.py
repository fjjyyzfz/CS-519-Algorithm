from collections import defaultdict
from heapq import heappush, heappop, heapify
import random

def best(rna):
    checklist = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
    length = len(rna)
    opt = defaultdict(lambda :(0, ""))
    for i in range(length):
        opt[i, i] = (0, ".")
    for d in range(1, length):
        #print(d)
        for i in range(length - 1):
            j = i + d
            if j <= length - 1:
                if rna[i] + rna[j] in checklist:
                    opt[i, j] = (opt[i + 1, j - 1][0] + 1, "(" + opt[i + 1, j - 1][1] + ")")
                    #print(opt)
                for k in range(i, j):
                    if opt[i, k][0] + opt[k + 1, j][0] > opt[i, j][0]:
                        opt[i, j] = (opt[i, k][0] + opt[k + 1, j][0], opt[i, k][1] + opt[k + 1, j][1])
                if opt[i, j][0] == 0:
                    opt[i, j] = (0, "."*(j - i + 1))
    return opt[0, length - 1]

def total(rna):
    checklist = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
    length = len(rna)
    opt = defaultdict(int)
    for i in range(length + 1):
        opt[i, i] = 1
        opt[i, i - 1] = 1
    for distance in range(1, length):
        for i in range(length - 1):
            j = i + distance
            if j <= length - 1:
                opt[i, j] += opt[i + 1, j]
                #opt[i, j] += 1
                for k in range(i + 1, j + 1):
                    if rna[i] + rna[k] in checklist:
                        opt[i, j] += opt[i + 1, k - 1] * opt[k + 1, j]
    return opt[0, length - 1]


def kbest(rna, num):
    checklist = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
    length = len(rna)
    opt = defaultdict(list)
    for i in range(length + 1):
        opt[i, i].append((0, "."))
        opt[i, i - 1].append((0, ""))

    def trypush(l, count1, count2):
        if (l, count1, count2) not in used and count1 < len(opt[i + 1, l - 1]) and count2 < len(opt[l + 1, j]):
            heappush(heap, (- opt[i + 1, l - 1][count1][0] - opt[l + 1, j][count2][0] - 1, l, count1, count2))
            used.add((l, count1, count2))
        
    def trypush_allunpair(count):
        if count < len(opt[i + 1, j]):
            heappush(heap, (- opt[i + 1, j][count][0], count))

    for d in range(1, length):
        for i in range(length - 1):
            j = i + d
            if j <= length - 1:
                heap, pair_tag_list = [], set()
                used = set()
                for l in range(i + 1, j + 1):
                    if rna[i] + rna[l] in checklist:
                        heap.append((- opt[i + 1, l - 1][0][0] - opt[l + 1, j][0][0] - 1, l, 0, 0))# pair with l                  
                        used.add((l, 0, 0))
                heap.append((- opt[i + 1, j][0][0], 0))# unpair with any one
                heapify(heap)
                while len(opt[i, j]) < num and heap:
                    output_list = heappop(heap)
                    if len(output_list) == 2:
                        num_pair, count = output_list
                        tag = "." + opt[i + 1, j][count][1]
                        if (tag) not in pair_tag_list:
                            opt[i, j].append((-num_pair, tag))
                            pair_tag_list.add((tag))
                            trypush_allunpair(count + 1)
                    else:
                        num_pair, l, count1, count2 = output_list
                        tag = "(" + opt[i + 1, l - 1][count1][1] + ")" + opt[l + 1, j][count2][1]
                        if (tag) not in pair_tag_list:
                            opt[i, j].append((-num_pair, tag))
                            pair_tag_list.add((tag))
                            trypush(l, count1 + 1, count2)
                            trypush(l, count1, count2 + 1)
    return opt[0, length - 1]



if __name__ == "__main__":
    print(kbest("GUUG", 10))

    # print(kbest("ACAGU", 10))
    # print(kbest("AC", 10))
    # print(kbest("GUAC", 10))
    # print(kbest("GCACG", 10))

    # print(kbest("CCGG", 10))#4
    # print(kbest("CCCGGG", 10))#20
    # print(kbest("UUCAGGA", 10))#11

    #print(kbest("AUAACCUA", 10))
    #print(kbest("UUGGACUUG", 10))
    #print(kbest("UUUGGCACUA", 10))
    # print(kbest("GAUGCCGUGUAGUCCAAAGACUUC", 10))
    # print(kbest("AGGCAUCAAACCCUGCAUGGGAGCG", 10))

    # print(kbest("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU", 10))
    #print(kbest("AGGCAUCAAACCCUGCAUGGGAGCGAGGCAUCAAACCCUGCAUGGGAGCGAGGCAUCAAACCCUGCAUGGGAGCG", 100))












