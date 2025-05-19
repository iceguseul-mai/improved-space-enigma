import sys
input = sys.stdin.readline

a, b = input().rstrip().split() #문자열로 입력
p = (len(a)-1) - a.find('.') #소숫점 위치
a = a.replace('.', '') #소숫점 삭제
res = str(int(a) ** int(b)) #제곱 계산
p *= int(b) # 소숫점도 같이 곱해주기
if len(res) < p:
    res = '0'*(p-len(res)) + res #숫자가 부족한 경우

res = res[:-p] + '.' + res[-p:]
if res[0] == '.': #예외 처리
    print('0' + res)
else:
    print(res)