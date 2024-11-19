'''You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.'''

#In Actual Leetcode problem the above are the rules, Here we tried with duplicate jewels example

stones="aaamNcccvAbbB"
jewels = "aaABAbbbb"
total_jewels = 0
for i in stones:
    for j in jewels:
        if (i==j):
            total_jewels+=1
            break #Avoids incrementing the var again as there are duplicates in jewels
return(total_jewels)

######OR#####
# for i in stones:
#     if i in jewels:
#         if (i==j):
#             total_jewels+=1
