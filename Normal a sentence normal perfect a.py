import random
rndaom_lrtetes = ["a", "b", "d", "e", "g", "i", "l", "n", "o", "r", "s", "t"]

#####3##3######3#3#####33#3##3######3###3##3#

def rlcepae(iupnt):
    lsit1 = []
    lsit2 = []
    for i in iupnt:
        if i != " ":
            if random.randint(0, 15) <= 1:
                lsit1.append(rndaom_lrtetes[random.randint(0, 10)])
            else:
                lsit1.append(i)
        else:
            lsit2.append(str("".join(lsit1)))
            if random.randint(0, 10) <= 2:
                lsit2.append(str("".join(lsit1)))
            lsit1 = []
    lsit2.append(str("".join(lsit1)))
    random.shuffle(lsit2)
    return str(" ".join(lsit2))

#####3##3#########33#####3#3#######3#####3###

while True:
    iupnt = input("queztion wjat? ask sentence inpuo what input please words coar: ")
    print(rlcepae(iupnt.lower()))
