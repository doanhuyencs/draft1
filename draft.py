thickness = int(input()) #This must be an odd number
c = 'H'

for i in range((thickness+1)//2):
    print((c*thickness*5).ljust(thickness))   