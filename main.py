from scipy.sparse import dok_matrix
from math import log
from math import pow
from math import sqrt


def norm(A, n, docn, q):
    nq = 0.0
    for i in range(0, n):
        nq += pow(q[i], 2)
    nq = sqrt(nq)
    for i in range(0, n):
        q[i] /= nq
    ndj = [0.0] * docn
    for value in A.keys():
        ndj[value[1]] += pow(A[value], 2)
    for i in range(0, docn):
        ndj[i] = sqrt(ndj[i])
    for value in A.keys():
        A[value] /= ndj[value[1]]


def get_cor2(A, n, docn, q):
    cos = [0.0] * docn
    for value in A.keys():
        cos[value[1]] += q[value[0]] * A[value]
    return cos


def get_cor(A, n, docn, q):
    cos = [0.0] * docn
    nq = 0.0
    ndj = [0.0] * docn
    numerator = [0] * n
    for i in range(0, n):
        nq += pow(q[i], 2)
    nq = sqrt(nq)
    for value in A.keys():
        ndj[value[1]] += pow(A[value], 2)
        numerator[value[1]] += q[value[0]] * A[value]
    for i in range(0, docn):
        ndj[i] = sqrt(ndj[i])
        cos[i] = numerator[i] / (nq * ndj[i])
    return cos


def inverse_document_frequency(A, docn, n):
    nw = [0] * n
    for value in A.keys():
        if A[value] > 0:
            nw[value[0]] += 1
    values = []
    for value in A.keys():
        idf = log(docn / nw[value[0]], 10)
        if idf != 0.0:
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
for spstr in input_line:
    try:
        ind = words.index(spstr)
        q[ind] += 1
    except ValueError:
        pass

cosphij = get_cor(A, n, docn, q)

#
print(cosphij)

norm(A, n, docn, q)

cosphij2 = get_cor2(A, n, docn, q)

print(cosphij2)
