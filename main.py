file = open("data.txt", "r")

docn = int(file.readline())

print("documents ", docn)

urls = []

for i in range(0, docn):
    urls.append(file.readline())

print(urls)

n = int(file.readline())

print("words ", n)

for i in range(0,n):
    print(file.readline())


