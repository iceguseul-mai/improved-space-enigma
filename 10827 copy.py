import sys
from decimal import Decimal, getcontext
input = sys.stdin.readline

a, b = map(str, input().split()) #문자열로 입력
getcontext().prec = 1101
print("{0:f}".format(Decimal(a)**int(b)))