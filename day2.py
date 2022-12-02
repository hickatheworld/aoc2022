f = open('./inputs/day2.txt')
lines = [l[:-1] for l in f.readlines()]

# Part 1
OPPONENT_MOVES ='ABC'
PLAYER_MOVES = 'XYZ'
def outcome(them, you): 
    x = OPPONENT_MOVES.index(them)
    y = PLAYER_MOVES.index(you)
    score = y + 1
    if x == y:
        score += 3
    elif (y + 2) % 3 == x:
        score += 6
    return score
total = 0
for l in lines:
    total += outcome(l[0], l[2])
print(total)

# Part 2
total = 0
for l in lines:
    them = l[0]
    order = l[2]
    i = OPPONENT_MOVES.index(them)
    match (order):
        case 'Y':
            move = PLAYER_MOVES[i]
        case 'X':
            move = PLAYER_MOVES[(i - 1) % 3]
        case 'Z':
            move = PLAYER_MOVES[(i + 1) % 3]
    total += outcome(them, move)
print(total)