def solution(h, q):
    p=[]
    for i in range(len(q)):
        head=2**h-1
        if q[i]==head: p.append(-1)
        else:
            j=h-1           #j=search level, 1 down from top
            while j>0: 
                par,l,r = head,head-2**j,head-1
                while True:
                    if q[i]==l or q[i]==r:
                        p.append(par)
                        j=0
                        break
                    elif q[i]<l: head=l     #search left
                    else: head=r            #search right
                    j-=1                    #next level down
                    par,l,r = head,head-2**j,head-1
    return p

p=solution(3,[7, 3, 5, 1])
