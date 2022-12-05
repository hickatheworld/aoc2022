f = open('./inputs/day4.txt')
lines = [l[:-1] for l in f.readlines()]

# Part 1
s = 0
for l in lines: 
    split = l.split(',')
    ranges = [
        [int(n) for n in split[0].split('-')],
        [int(n) for n in split[1].split('-')]
    ]
    # x is the index of the longuest section assigment
    x = 0 if abs(eval(split[0])) >= abs(eval(split[1])) else 1
    # y is the other index
    y = (x + 1) % 2
    if ranges[x][0] <= ranges[y][0] and ranges[x][1] >= ranges[y][1]:
        s+=1
print(s)