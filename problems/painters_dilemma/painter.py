def main():

        tests = int(input())
        
        for i in range(tests):
                brush1 = 0
                brush2 = 0
                changes = 0;
                numc = int(input())
                clrs = input()
                clrs = clrs.split(" ")
                for k in range(numc):
                        clrs[k] = int(clrs[k])

                #print(clrs)
                for j in range(numc):
                        searchList = clrs[j:]
                        #print(searchList)
                        if((searchList[0] == brush1) or (searchList[0] == brush2)):
                            #if (searchList[0] == brush1):
                                #print("brush1 already prepped.")
                            #if (searchList[0] == brush2):
                                #print("brush2 already prepped.")
                            continue
                        ind1 = -1
                        ind2 = -1
                        p1canchange = False
                        p2canchange = False
                        try:
                                ind1 = searchList.index(brush1)
                        except ValueError:
                                p1canchange = True
                                #print(str(brush1) + " not found later in list.")
                        try:
                                ind2 = searchList.index(brush2)
                        except ValueError:
                                p2canchange = True
                                #print(str(brush2) + " not found later in list.")

                        if (p1canchange == False and p2canchange == False):
                                #get the smaller of the 2 indices
                                if(ind1 > ind2):
                                        p1canchange = True
                                else:
                                        p2canchange = True
                        if (p1canchange):
                                brush1 = searchList[0]
                                changes += 1
                                continue
                                #print("brush1 changed to " + str(brush1) + ", changes: " + str(changes))
                        if (p2canchange):
                                brush2 = searchList[0]
                                changes += 1
                                #print("brush2 changed to " + str(brush2) + ", changes: " + str(changes))

                print(changes)

main()
