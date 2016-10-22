cases = int(input())
for i in range(cases):
    games = int(input())
    moves = 0
    for j in range(games):
        piles = int(input())
        buff = input().split(' ')
        for k in buff:
            moves += ((int(k) - 1) / 2)
    if moves % 2 == 0:
        print('Bob')
    else:
        print('Alice')