from scipy.sparse import dok_matrix
from math import log


def inverse_document_frequency(A, docn, n):
    nw = [0] * n
    for value in A.keys():
        if A[value] > 0:
            nw[value[0]] += 1
    values = []
    for value in A.keys():
        idf = log(docn / nw[value[0]], 10)
        if (idf != 0.0):
            A[value[0], value[1]] *= idf
        else:
            values.append(value)
    for val in values:
        A[val] = 0.0
    print("inverse document frequency done")

file = open("data.txt", "r")

docn = int(file.readline())

print("documents ", docn)

urls = []

for i in range(0, docn):
    urls.append(file.readline())

print(urls)

n = int(file.readline())

print("words ", n)

words = []

A = dok_matrix((n, docn), dtype=float)

for i in range(0, n):
    line = file.readline()
    tmp = line.split(" ")
    words.append(tmp[0])
    for j in range(1, len(tmp) - 1):
        val = tmp[j]
        tmp2 = val.split(":")
        dok = int(tmp2[0])
        cnt = int(tmp2[1])
        A[i, dok] = cnt

print("data loaded")
inverse_document_frequency(A, docn, n)

print("enter words")

input_line = input()

input_line = input_line.split(" ")

q = [0] * n
for str in input_line:
    try:
        ind = words.index(str)
        q[ind] += 1
    except ValueError:
        pass
