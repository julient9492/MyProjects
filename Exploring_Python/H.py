thickness = 5
c = 'H'
for i in range(thickness):
    print((c*i*2+c).center(2*thickness-1))

for i in range(thickness):
    print((thickness*c).center(2*thickness-1) + (thickness*c).center(5*thickness))
for i in range((thickness+1)//2):
    print((5*thickness*c).center(6*thickness))
for i in range(thickness):
    print((thickness*c).center(2*thickness-1)+ (thickness*c).center(5*thickness))
for i in range(thickness):
    print((c*((2*thickness-1)-2*i)).center(2*thickness-1).rjust(5*thickness))