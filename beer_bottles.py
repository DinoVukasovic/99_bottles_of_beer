def beer_sing(i, end):
    print(i or 'No more', 'bottle' + ('s' if i - 1 else ''), end)


for i in range(99, 0, -1):
    beer_sing(i, 'of beer on the wall,')
    beer_sing(i, 'of beer,')
    print('Take one down, pass it around,')
    beer_sing(i - 1, 'of beer on the wall.\n')