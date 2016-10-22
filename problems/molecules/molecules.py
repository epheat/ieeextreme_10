buff = input()
buff = buff.split(' ')
c = float(buff[0])
h = float(buff[1])
o = float(buff[2])


d = ( o - (h/2)) / 2
g = (c - ((o - (h/2))/2) ) / 6
w = (h/2) - c + d


"""
g = 0

while(h >= 12 and c >= 6 and o >= 6):
    c -= 6
    h -= 12
    o -= 6
    g += 1


w = h / 2
d = c
"""
if w % 1 != 0 or g % 1 != 0 or c % 1 != 0:
    print('Error')
else:
    print(str(int(w)) + " " + str(int(d)) + " " + str(int(g)))