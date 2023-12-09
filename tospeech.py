file = open("musicians.txt","r")
"""
members = ["John","Paul","Cheryl","Ida"]
instruments = ["guitar","bass","vocals","drums"]
primeKoalas = [members,instruments]

for i in range (4):
    
    
    output = str((primeKoalas[0][i], primeKoalas[1][i]))+"\n"
   
    file.write(output )
    """
def tospeech(inc):
    print(inc +"!")
for line in (file):
    tospeech(line)
file.close()

