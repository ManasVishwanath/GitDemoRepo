

inputString = "sdjsiofewiohfdbvuehfsdbvdspS SHDJKDSF DFHJDFKS 83749HDFD "
#gIVE ME CHARACTER WHICH IS COMING HIGHEST nO OF TIMES IN ABOVE STRING

k = {}

for char in inputString:
    if char in k.keys():
        k[char] = k[char] + 1
    else:
        k[char] = 1


res = sorted(k.items() , key= lambda x:x[1],reverse=True)[0][0]
print(res)


