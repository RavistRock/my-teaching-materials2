file = open("C:/Users/teacher/Downloads/26_11811.txt")
N, R = (int(x) for x in file.readline().split())
l_r = 0
a, b = 0, 0
lst = []
for x in file:
    l, r = (int(i) for i in x.split())
    lst.append([l, r])
lst.sort()

print(lst)
