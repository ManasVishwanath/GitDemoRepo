

inputString = "sdjsiofewiohfdbvuehfsdbvdspS SHDJKDSF DFHJDFKS 83749HDFD "
#gIVE ME CHARACTER WHICH IS COMING HIGHEST nO OF TIMES IN ABOVE STRING

k = {}

for char in inputString:
    if char in k.keys():
        k[char] = k[char] + 1
    else:
        k[char] = 1


for i in k.values():


