def splits(diffs, num_walkers):
    if num_walkers == 0:
        cuts.append(len(dogs_size) - 1)
        return cuts

    max_val = max(diffs)
    max_ind = diffs.index(max_val)
    cuts.append(max_ind)
    diffs[max_ind] = -1
    #print("splits @ walkers " + str(num_walkers))
    #print(diffs)
    return splits(diffs, num_walkers - 1)

def getDiffs(dogs):
    diffs = []
    for i in range(1,len(dogs)):
        diffs.append(dogs[i] - dogs[i - 1])
    return diffs

t = int(input())
for i in range(t):
    cuts = []
    dogs_size = []
    buff = input()
    buff = buff.split(' ')
    dogs = int(buff[0])
    walkers = int(buff[1])
    for k in range(dogs):
        dogs_size.append(int(input()))
    dogs_size.sort()
    #print("dogs")
    #print(dogs_size)
    if walkers >= dogs:
        print('0')
    else:
        thediffs = getDiffs(dogs_size)
        chops = splits(thediffs, walkers - 1)
        chops.sort()
        #print("final splits")
        #print(chops)
        strt = 0
        total = 0
        for j in chops:
            groups = dogs_size[strt:j + 1]
            strt = j + 1
            #print("group")
            #print(groups)
            total += (groups[len(groups)-1] - groups[0])
        print(total)
