f = open('./inputs/day3.txt')
lines = [l[:-1] for l in f.readlines()]

s = 0
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for l in lines:
    for c in l[:len(l)//2]:
        if c in l[len(l)//2:]:
            s += alphabet.index(c) + 1
            break
print(s)