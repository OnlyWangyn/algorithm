def isIsomorphic(s,t):
    ssize = len(s)
    tsize= len(t)
    records = {}
    if ssize !=tsize:
        return False
    for i in range(0,ssize):
        num=[]
        num.append(s[i])
        num.append(t[i])
        records[i]=num
    for i in records:
        r = records[i]
        value1 = r.pop()
        value2 = r.pop()
        k = i+1
        while k < len(records):
            rk = records[k]
            valuek1 = rk.pop()
            valuek2 = rk.pop()
            if(value1 == valuek1 and value2!=valuek2) or (value1!=valuek1 and value2 == valuek2):
                return False
            k +=1
    return True
print isIsomorphic('add','egg')
#print isIsomorphic('a`%ii,VEZQc_BSU%ObO5<sX81B/bOw+CNUd#Uav*P!Ax!#>hh,k#b/|>4ixFQZl+l!?bJjakbQbGglEb<g>Hf81m@A9GIvbd]qh?y__t+E(Iyv7zUEfZF{81VaM-0u?]tG=_fFR/XJ=X{-,oRpxE9u*VNYlM','b`%ii-WE[Qc_BSV%OcO5<sX82B/cOw+CNVd#Vbv*P!Bx!#?hh-k#c/|?4ixFQ[l+l!?cJkbkcQcGhlEc<h?Hf82m@B9GIvcd]rh?y__t+E(Iyv7{VEf[F{82WbN/0u?]tG=_fFR/XJ=X{/-oRpxE9u*WNYlN')

