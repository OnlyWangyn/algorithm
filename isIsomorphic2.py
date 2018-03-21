def isIsomorphic(s,t):
    ssize = len(s)
    tsize= len(t)
    records = {}
    string = ''
    if ssize !=tsize:
        return False
    for i in range(0,ssize):
        sc = s[i]
        tc = t[i]
        if sc not in records.keys():
            if tc in string:
                return False
            records[sc] = tc
            string = string + tc
        else:
            value = records[sc]
            if(value!=tc):
                return False
    return True

print isIsomorphic('polpk','optot')
#print isIsomorphic('a`%ii,VEZQc_BSU%ObO5<sX81B/bOw+CNUd#Uav*P!Ax!#>hh,k#b/|>4ixFQZl+l!?bJjakbQbGglEb<g>Hf81m@A9GIvbd]qh?y__t+E(Iyv7zUEfZF{81VaM-0u?]tG=_fFR/XJ=X{-,oRpxE9u*VNYlM','b`%ii-WE[Qc_BSV%OcO5<sX82B/cOw+CNVd#Vbv*P!Bx!#?hh-k#c/|?4ixFQ[l+l!?cJkbkcQcGhlEc<h?Hf82m@B9GIvcd]rh?y__t+E(Iyv7{VEf[F{82WbN/0u?]tG=_fFR/XJ=X{/-oRpxE9u*WNYlN')

