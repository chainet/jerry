num_lines = int(input('你想要多少行星星？'))
num_stars = int(input('你想要多少个星星？'))
for line in range(0,num_lines):
    for star in range(0,num_stars):
        print('*', end='')
    print('')