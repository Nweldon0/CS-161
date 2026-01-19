#Num = 31
#Num = 1.825
#The error message states that it cannot get a binary value from a float
#This is because the number 1.825 is not an integer, and therefore must be a float
NumX = 18
NumY = 0b1011
NumZ = 0xA3
#print (NumX, bin(NumX), hex(NumX))
#print (NumX, NumY, NumZ)
print(f"{NumX} + {NumY} + {NumZ} = {NumX + NumY + NumZ}")

#Using empty lines to space out the different sections
for i in range(3):
    print("")

OrigS = 240
DictS = 25
CompS = 148

PercS = round(1 - ((CompS + DictS) / OrigS), 4)
#I chose to move the semicolons forward instead of the words because I thought it looked nicer
print(f"Compressed text size  : {CompS} characters")
print(f"Dictionary size       : {DictS} characters")
print(f"Total                 : {CompS + DictS} characters")
print("")
print(f"Original text size    : {OrigS} characters")
print(f"Compression           : {PercS * 100}%")

for i in range(3):
    print("")

Numbin = int(input("Enter a number: "))
print(bin(Numbin & 0xFF)[2:].zfill(8))
#I didn't even know "zfill" was a command, the autofill suggested it
#It seems to ensure you get a full eight numbers, adding zeros on the left to fill the full binary number