file = open("musicians.txt","w")
"""
primeKoalas =[]
primeKoalas[0,0] = "John"
primeKoalas[1,0] = "Paul"
primeKoalas[2,0] = "Cheryl"
primeKoalas[3,0] = "Ida"
primeKoalas[0,1] = "guitar"
primeKoalas[1,1] = "bass"
primeKoalas[2,1] = "vocals"
primeKoalas[3,1] = "drums"
print(primeKoalas)
"""
members = ["John","Paul","Cheryl","Ida"]
instruments = ["guitar","bass","vocals","drums"]
primeKoalas = [members,instruments]
#print (instruments[0])
#print (primeKoalas)
#print (primeKoalas[0][0])
#print(len(members))
for i in range (4):
    #print (i)
    print (primeKoalas[0][i], primeKoalas[1][i])
    output = str((primeKoalas[0][i], primeKoalas[1][i]))+"\n"
    print (output)
    file.write(output )
file.close()
