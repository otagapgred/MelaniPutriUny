des=int(input('Ängka desimal : '))
a=[]
i=0
while des>0:
    a.append(des % 2)
    des=des//2
    i=i+1
if len(a)<8:
    ces=8-len(a)
    binter= '0 '*ces
elif len(a)==8:
    binter=''    
print("hasil biner = ",binter, end='')

for i in range(i-1, -1, -1):
    print(a[i], end=' ')

print("\nHasil Oktal = ", oct(des))
print("Hasil Hexadesimal = ", hex(des))
    
 