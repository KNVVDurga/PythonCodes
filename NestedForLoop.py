stones="aaamNcccvAbbB"
jewels = "aaABAbbbb"
total_jewels = 0
for i in stones:
    for j in jewels:
        if (i==j):
            total_jewels+=1
            break
return(total_jewels)

######OR#####
# for i in stones:
#     if i in jewels:
#         if (i==j):
#             total_jewels+=1
