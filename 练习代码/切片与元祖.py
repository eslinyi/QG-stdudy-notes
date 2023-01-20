players = ['Charles', 'marina', 'michael', 'florence', 'erl', 'happu', 'djaiudj']

print(players)  # 暂时排序
print(sorted(players))
print(sorted(players, reverse=True))

players.sort()  # 永久排序正反
print(players)
players.reverse()
print(players)

happy_players = players[:]  # 切片复制

players.append('quqi')  # 复制检验+循环
happy_players.append('ice cream')
for player in players:
    print('you are good:')
    print(player + '\n')

for happy_player in happy_players:
    print('my friend like:')
    print(happy_player + '\n')

dimensions = [20, 200, 100]  # 元组与元组修改
print('old vacation:')
for dimension in dimensions:
    print(dimension)

dimensions = [10, 100, 1000]
print('\nnew vacation:')
for dimension in dimensions:
    print(dimension)

for player in players:  # if语句
    if player == 'Charles':
        print(player.lower())
    else:
        print(player.title())