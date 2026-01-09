def fibonachchi(n):
    # n=1 #[1]
    # n=2 #[1]
    # n=3 #[1,1,2]
    # n=4 #[1,1,2,3]
    # n=5 #[1,1,2,3,5]
    sonlar=[]
    a,b=0,1
    for i in range(n):
        sonlar.append(a)
        a,b=b,a+b
    return sonlar
print(fibonachchi(n=5))
