#NOTE: importing the library is VERY important for this question!
#Further readng: https://en.wikipedia.org/wiki/Regular_expression
#Python documentation: https://docs.python.org/2/library/re.html

import re

T = int(input())
for i in range(T):
    try:
        re.compile(input())
        print ("True")
    except re.error:
        print ("False")
        
