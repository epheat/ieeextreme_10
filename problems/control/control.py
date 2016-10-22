def test3(vals, mean, std):
    boundU = mean + (3 * std)
    boundL = mean - (3 * std)
    for i in vals:
        if i > boundU or i < boundL:
            return False
    return True

def test2(vals, mean, std):
    #At least two out of three successive values fall on the same side of, 
    #and more than two sigma units away from, the center line.
    
    boundU = mean + (2 * std)
    boundL = mean - (2 * std)
    
    for i in range(2, len(vals)):
        if vals[i] > boundU:
            if vals[i-1] > boundU or vals[i-2] > boundU:
                return False
        elif vals[i] < boundL:
            if vals[i-1] < boundL or vals[i-2] < boundL:
                return False
    return True

#At least four out of five successive values fall on the same side of, 
#and more than one sigma unit away from, the center line.
def test1(vals, mean, std):
    boundU = mean + std
    boundL = mean - std
    above = []
    below = []
    for i in range(0,len(vals)):
        if vals[i] > boundU:
            above.append(i)
        if vals[i] < boundL:
            below.append(i)
    for i in range(4, len(above)):
        if (above[i] - above[i-4]) < 5 or (above[i] - above[i-3]) < 5:
            return False
    for i in range(4, len(below)):
        if (below[i] - below[i-4]) < 5 or (below[i] - below[i-3]) < 5:
            return False
    return True


#At least eight successive values fall on the same side of the center line.
def test(mean, vals):
    above = 0
    below = 0
    for i in vals:
        if i < mean:
            below += 1
            above = 0
        if i > mean:
            below = 0
            above += 1
        if above >= 8 or below >= 8:
            return False
        
    return True

def main():
    cases = int(input())
    """
    Size of group (n)      A2
        2                1.880
        3                1.023
        4                0.729
        5                0.577
        6                0.483
        7                0.419
        8                0.373
        9                0.337
       10                0.308
    """

    a = [1.88,1.023,.729,.577,.483,.419,.337,.308]

    for m in range(cases):
        vals = []
        sub_avg = []
        sub_range = []
        avg_avg = 0
        avg_range = 0
        vals = input()
        vals = vals.split(' ')
        num_points = int(vals[0])
        sub_size = int(vals[1])
        a2 = a[sub_size - 2]
        vals = vals[2:]
        for i in range(0, len(vals)):
            vals[i] = int(vals[i])
        count = 0
        curr_range = []
        for j in vals:
            curr_range.append(j)
            count += 1
            if count == sub_size:
                sub_avg.append(float(sum(curr_range))/float(sub_size))
                sub_range.append(max(curr_range)-min(curr_range))
                count = 0
                curr_range = []
        if count != 0:
            sub_avg.append(float(sum(curr_range))/float(count))
            sub_range.append(max(curr_range)-min(curr_range))
        if len(sub_avg) > 0:
            avg_avg = (float(sum(sub_avg))/float(len(sub_avg)))
        if len(sub_range) > 0:
            avg_range = (float(sum(sub_range))/(float(len(sub_range))))

        """
        #UCLX = Xave + A2 Rave

        #LCLX = Xave - A2 Rave

        #CLX = Xave
        """
        UCLX = avg_avg + (a2 * avg_range)
        LCLX = avg_avg - (a2 * avg_range)
        std = (UCLX - avg_avg) / 3.0
        cond = test3(vals, avg_avg, std) and test2(vals, avg_avg, std) and test1(vals, avg_avg, std) and test(avg_avg, vals)
        if cond:
            print("In Control")
        else:
            print("Out of Control")

main()    
