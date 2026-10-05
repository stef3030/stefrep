def wizards(N,start,duels):
    owner = start
    changed_hands = 1
    #print(duels([0],[1]))
    if (duels([0][1]))==owner:
     owner = duels [0][0]
     changed_hands+=1
     print(owner)
    if (duels([0][0]))==owner:
        owner=duels[1][0]
        changed_hands+=1
        print(owner)
    if (duels([2][0]))==owner:
       owner=duels[2][0]
       changed_hands+=1
       print(owner)



wizards (3, "A", ["BA","CB","DA"])