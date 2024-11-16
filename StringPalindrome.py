s = "ABCD"
rev = ""
l = len(s)
for i in range(l-1,-1,-1):
    rev = rev+s[i]
    # print(rev)
# print(rev)
    
if (s==rev):
    print("Palindrome")
else:
    print("Not a Palindrome")
