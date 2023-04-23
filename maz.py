w=11
h=9
maz=[]
for i in range(h):
    maz.append([0]*w)
for x in range(w):
    maz[0][x]=1
    maz[h-1][x]=1
for y in range(h):
    maz[y][0]=1
    maz[y][w-1]=1
#maz[5][7]=1
#print(maz)     
for x in range(1,w-1):
    for y in range(1,h-1):
        maz[y][x]=0

print(maz)    