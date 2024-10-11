import argparse 
import os
import regex as re
import html


MIN_CHARS = 1
MAX_CHARS = 5000



def check_brackets(string):
    
    a = []
    surrounding = False

    for i, ch in enumerate(string):
        
        if ch == '{':
            if i>0 and string[i-1]=='\\':
                continue
            else:
                a.append(1)
            if i == 0:
                surrounding=True

        elif ch=='}':
            if i>0 and string[i-1]=='\\':
                continue
            else:
                a.append(-1)
          
    b = sum(a)
    if len(a) >= 1 and b != 0:
        raise ValueError(string)
    surrounding = (surrounding and string[-1]=='}')
    if not surrounding:
        return string
    elif (b == 0) == 1:
        return string[1:-1]
    else:
        return string


print(check_brackets("ofhowgo\\{ wkfm"))

            
            
