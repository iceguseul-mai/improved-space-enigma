# import sys
# input = sys.stdin.readline

s = input()
B = "toycartoon"
if s[0] in "toycartoon":
    i = B.find(s[0]) 
    if i != -1:
        result = B[:i] + s + B[i+1:]
    else:
        result = B+'_'+s

if len(result) > 20:
    print("toycartoon")
else:
    print(result)