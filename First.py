

inputString = "sdjsiofewiohfdbvuehncuidhds98d9f8dyfhdsfldsk fjsajdksgjhdhsakjdsh dlksa djaslkdhask89djksds fsdbvdspS SHDJKDSF DFHJDFKS 83749HDFD "
#gIVE ME CHARACTER WHICH IS COMING HIGHEST nO OF TIMES IN ABOVE STRING

k = {}

for char in inputString:
    if char in k.keys():
        k[char] = k[char] + 1
    else:
        k[char] = 1

print(k)
repeated = max(k, key = k.get)
print(repeated, k[repeated])


