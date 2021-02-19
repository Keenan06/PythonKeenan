places = ['new york', 'cape town', 'london', 'boston', 'joburg']
print(places)
print(sorted(places))
places.sort(reverse=True)
print(places)
places.sort(reverse=False)
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3.10
games = ['call of duty', 'assasins creed', 'farcry', 'gears of war', 'killzone']
print(sorted(games))
games.sort(reverse = True)
print(games)
games.pop(3)
print(games)
games.sort()
print(games)
games.insert(3, 'ratchet and clank')
print(games)
print(len(games))
games.append('fifa')
print(games)
del games[2]
print(games)
