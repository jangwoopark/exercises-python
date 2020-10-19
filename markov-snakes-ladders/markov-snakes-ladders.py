import random
def roledice(prob):
    proba = [(int)(i*100) for i in prob]
    newlist = []
    for i in range(6):
        newlist += [i+1] * proba[i]
    return random.choice(newlist)

def playgame(prob, snake_start, snake_end, ladder_start, ladder_end):
    current = 1
    rolls = 0
    count = [0, 0, 0, 0, 0, 0]
    while current != 100:
        dice = roledice(prob)
        count[dice-1] += 1
        current += dice
        if current in snake_start:
            index = snake_start.index(current)
            current = snake_end[index]
        if current in ladder_start:
            index = ladder_start.index(current)
            current = ladder_end[index]
        if current > 100:
            current -= dice
        rolls += 1
    return rolls

n = (int)(input())
for _ in range(n):
    prob = list(map(float, input().split(',')))
    no_ladders, no_snakes = list(map(int, input().split(',')))
    sna = list(input().split(' '))
    snake_start, snake_end = [], []
    for i in range(len(sna)):
        x, y = list(map(int, sna[i].split(',')))
        snake_start.append(x)
        snake_end.append(y)

    lad = list(input().split(' '))
    ladder_start, ladder_end = [], []
    for i in range(len(lad)):
        x, y = list(map(int, lad[i].split(',')))
        ladder_start.append(x)
        ladder_end.append(y)

    output = 0
    for i in range(500):
        output += playgame(prob, snake_start, snake_end, ladder_start, ladder_end)
    print((int)(output/500))
