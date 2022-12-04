f = open('./inputs/day3.txt')
lines = [l[:-1] for l in f.readlines()]
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
s = 0
for l in lines:
    for c in l[:len(l)//2]:
        if c in l[len(l)//2:]:
            s += alphabet.index(c) + 1
            break
print(s)

# Part 2
s = 0
for i in range(0, len(lines), 3):
    for c in lines[i]:
        if c in lines[i + 1] and c in lines[i + 2]:
            s += alphabet.index(c) + 1
            break
print(s)