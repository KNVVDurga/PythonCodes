def scoreOfString(s):
    sum = 0
    for i in range(len(s)-1):
        diff = ord(s[i])-ord(s[i+1])
        if (diff<0):
            diff = diff*(-1)
            #diff = abs(diff)
        sum = sum+diff
    return(sum)

print(scoreOfString("abbs"))
