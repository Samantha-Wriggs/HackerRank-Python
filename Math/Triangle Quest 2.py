for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i - 1)//9)**2)

#Explanation: looking at the required output, it's important to notice that all the results are squares of 11, 111, 1111, etc.
#As such, we only need to find a formula that, for each iteration of i, gives us the appropriate 'number of 1s' and then square it.
#Ie, for i = 3, we have 10^3 = 1000. 1000//9 = 111. 111^2 = 12321.
