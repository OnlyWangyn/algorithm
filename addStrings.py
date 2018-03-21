import sys
def addStrings(num1,num2):
    size1 = len(num1)
    size2 = len(num2)
    if size1 == 0:
        return num2
    if size2 == 0:
        return num1
    size = max(size1,size2)
    result = []
    carry = 0
    while size1 or size2 or carry:
        digital = carry
        if size1:
            size1-=1
            digital +=ord(num1[size1]) - ord('0')
        if size2:
            size2 -=1
            digital += ord(num2[size2])-ord('0')
        carry = digital > 9
        result.append(str(digital %10))
    return ''.join(result[::-1])
print addStrings('123','46')
