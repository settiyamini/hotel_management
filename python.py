x=int(input('Enter divident'))
y=int(input('Enter divisor'))
q=x//y
def makearry(q):
    arr=[]
    while q:
        a=q%10
        arr.append(a)
        q=q//10
    arr=arr[::-1]
    return arr
def converttonum(arr):
    num=0
    for i in arr:
        num=num*10+i
    return num
c=makearry(q)
dividentarray=makearry(x)
placedivident=0
print(c)
print(y,')',x,'(',q)
space=" "
placement=3
count=0
for i in c:
    if count>0:
        valind=converttonum(dividentarray[placedivident:placedivident+place])
        ans=valind-val
        dist=space*placement
        print(dist,end="")
        if count==1:
            placedivident+=place-1
    val=i*y
    arr=makearry(val)
    place=len(arr)
    dist=space*placement
    if count>0:
        if ans==0:
            pn=converttonum(dividentarray[placedivident:placedivident+place])
            placedivident+=place
        else:
            ln=len(makearry(ans))
            pn=converttonum(dividentarray[placedivident:placedivident+place-ln])
            placedivident+=place-ln
    print(dist,val)
    print('----------')
    placement+=place
    count+=1
    
k=space*placement
print(k,x%y)