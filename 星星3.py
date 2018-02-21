num_blocks = int(input('你想要几个星星块？'))
num_lines = int(input('你想要星星块里有几行？'))
num_stars = int(input('你想要星星块里一行里有几个星星？'))
for block in range(0,num_blocks):
    for line in range(0,num_lines):
        for star in range(0,num_stars):
            print('*',end=' ')
        print(' ')
    print(' ')