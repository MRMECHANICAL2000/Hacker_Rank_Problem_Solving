####Use PYPY3 not python 3 to avoid time limit exided error

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    matrix=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s1)-1,-1,-1):
            if s1[i]==s2[j]:
                matrix[i][j]=1+matrix[i+1][j+1]
            else:
                matrix[i][j]=max(matrix[i+1][j],matrix[i][j+1])

    return(matrix[0][0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()