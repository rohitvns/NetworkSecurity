# ROHIT SINGH
# 2019135

def inv(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1