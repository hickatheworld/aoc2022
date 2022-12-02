f = open('./inputs/day1.txt')
lines = [l[:-1] for l in f.readlines()]

# Part 1
max_cals = 0
current = 0
for l in lines:
    if l == '':
        if current > max_cals:
            max_cals = current
        current = 0
    else:
        current+= int(l)
print(max_cals)

# Part 2

max_cals = [0, 0, 0]
current = 0
for l in lines:
    if l == '':
        for i in range(len(max_cals)):
            if current > max_cals[i]:
                for j in range(len(max_cals) - 1, i, - 1):
                    max_cals[j] = max_cals[j - 1]
                max_cals[i] = current
                break
        current = 0
    else:
        current += int(l)
print(sum(max_cals))