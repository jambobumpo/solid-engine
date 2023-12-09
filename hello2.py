

def noSpace(string1):
    foundspace = False 
    length = len(string1)
    for i in range (0,length-1):
        print (string1[i])
        print (i)
        if string1[i] == " ":
            foundspace = True
            return False
    return True
        










while True:
    trackname = input("enter trackname")
    if noSpace(trackname) == True:
        print ("BALID")
        break
    else:
        print ("inbalid ender new trackname")
    











