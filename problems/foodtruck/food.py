from math import *
from operator import itemgetter

#d = 2 Ã r Ã arcsin (sqrt (sin2((lat1 - lat2)/2) + cos(lat1) Ã cos(lat2) Ã sin2((long1 - long2)/2)))

def degRad(deg):
    return pi * deg / 180

def calcDist(lat1, long1, lat2, long2):
    return (2 * 6378.137 * asin(sqrt((sin((lat1 - lat2)/2)**2) + (cos(lat1) * cos(lat2) * (sin((long1 - long2)/2)**2)))))

#10/21/2016 09:56
def timeComp(time1, time2):
    year1 = int(time1[6:10])
    year2 = int(time2[6:10])
    mon1 = int(time1[0:2])
    mon2 = int(time2[0:2])
    day1 = int(time1[3:5])
    day2 = int(time2[3:5])
    hr1 = int(time1[11:13])
    hr2 = int(time2[11:13])
    min1 = int(time1[14:16])
    min2 = int(time2[14:16])
    if year1 == year2:
        if mon1 == mon2:
            if day1 == day2:
                if hr1 == hr2:
                    return min1 > min2
                else:
                    return hr1 > hr2
            else:
                return day1 > day2
        else:
            return mon1 > mon2
    else:
        return year1 > year2;

def main():
    loc = input()
    mylat = float(loc.split(',')[0])
    mylon = float(loc.split(',')[1])
    radius = float(input())
    ugh = input()
    locs = []
    near = []
    while(True):
        buff = ""
        try:
            buff = input()
        except:
            break;
        newbuff = buff.split(',')
        time = newbuff[0]
        lat = float(newbuff[1])
        lon = float(newbuff[2])
        num = newbuff[3]
        """
        wasFound = False
        for i in range(0, len(locs)):
            if locs[i][3] == num:
                if timeComp(time, locs[i][0]):
                    locs[i] = (time,lat,lon,num)
                wasFound = True
                break
        if not wasFound:
            locs.append((time, lat, lon, num))
        """
        locs.append((time, lat, lon, num))
    
    locs.sort(key=lambda x: x[3]) 
    j = 1
    while j < len(locs):
        if locs[j][3] == locs[j-1][3]:
            if(timeComp(locs[j][0], locs[j-1][0])):
                del locs[j-1]
            else:
                del locs[j]
            j = j - 1
        j = j+1
        
    for i in locs:
        dist = calcDist(degRad(mylat), degRad(mylon), degRad(i[1]), degRad(i[2]))
        if dist <= radius:
            near.append(i[3])
    result = ""
    for i in range(0, len(near)-1):
        result += (near[i] + ",")
    result += near[len(near) -1]
    print(result)
    
       
main()