def mergeSortedArray(A, m, B, n):
    for j in range(n):
        num= B[j]
        for i in range(m+n):
            if num<A[i]:
                start=m+j
                while start>i:
                    A[start]=A[start-1]
                    start-=1
                A[i]=num
                break;
            elif i>=m+j:
                A[m+j]=num
                break
    return A
def mergeSortedArray2(A,m,B,n):
    i = m-1
    j = n-1
    position = m+n-1
    while j>=0:
        if A[i]>B[j] and i>=0:
            A[position] = A[i]
            i-=1
        else:
            A[position]=B[j]
            j-=1
        position-=1
    return A
A = [416,484,808,960,1340,1342,1618,1632,1841,1898,0,0,0,0,0,0,0,0,0,0,0,0]
B = [31,85,102,194,282,371,396,453,707,771,1619,1876]
print mergeSortedArray2(A,10,B,12)

