#-------------------------------------------------------------------------
# Name:       Question 1
# Purpose:    Nums 1-10, skip 7
# Author:     Mistry. R
# Created:    07/05/2024
#-------------------------------------------------------------------------

num = 0

while num < 11:
    print (num)
    num += 1

    if num == 7:
        num += 1
        continue

    