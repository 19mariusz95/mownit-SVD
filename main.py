from scipy.sparse import dok_matrix

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

for i in range(0,n):
    line = file.readline()
    tmp = line.split(" ")
    words.append(tmp[0])
    print(i, " ", n)
    for j in range(1, len(tmp) - 1):
        val = tmp[j]
        tmp2 = val.split(":")
        dok = int(tmp2[0])
        cnt = int(tmp2[1])
        A[i, dok] = cnt
