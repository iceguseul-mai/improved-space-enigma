import sys 
input = sys.stdin.readline

# course - 수강 과목 개수
# priority - 제일 낮은 단계를 제외한 우선순위 단계 개수
# limit - 각 우선순위 단계의 수용 한계
for _ in range(int(input())):
    course, priority = map(int,input().split())
    limit = list(map(int, input().split()))
    lv = list(map(int, input().split()))
    for i in lv:
        limit[i-1] -= 1
    op = 0
    while not len(set(lv)) <= 1:
        if op == 1000:
            print(-1)
            sys.exit(0)
        for i in range(n):
            if [lv[i]]