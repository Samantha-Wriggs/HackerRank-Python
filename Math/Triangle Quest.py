for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10, i)//9)*i)

#Explanation: Since you can't use strings, you aren't printing i multiple times. You're using the math above to get the equivalent number.
#Ie: If i = 3, we have 10^3 = 1000. 1000//9 = 111. 111 x 3 = 333. There are multiple ways to solve this.
