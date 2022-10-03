for i in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    D=list(map(int,input().split()))
    count=0
    temp=0
    for i in range(min(A),max(D)):
        count=0
        for j in range(len(D)):
            if D[j]>i+0.5 and i+0.5>A[j]:
                count+=1
        if count>temp:
            temp=count
    print(temp)
