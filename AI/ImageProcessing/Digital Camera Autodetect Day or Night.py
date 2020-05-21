# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

lines = stdin.read().splitlines()
r = []
g = []
b = []
for line in lines:
    l = list(line.split())
    for entry in l:
        rgb = list(map(int, entry.split(",")))
        b.append(rgb[0]/255)
        g.append(rgb[1]/255)
        r.append(rgb[2]/255)

R = sum(r)/len(r)
G = sum(g)/len(g)  #though len(g)= len(b)=len(r)
B = sum(b)/len(b)

Y = (R+R+B+G+G+G)/6

#print(Y)

if Y>0.3:
    print("day")
else:
    print("night")
