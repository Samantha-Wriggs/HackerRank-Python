def is_leap(year):
    
#Method 1
    leap = True
    
    if year%4 != 0:
        leap = False
    elif year%100 == 0:
        if year%400 == 0:
            leap = True
        else:
            leap = False
    return leap


#Method 2 
    #return (y%4==0)and(y%100!=0 or y%400==0)
    
    
    
year = int(raw_input())
print is_leap(year)
