s = input().rstrip()
ans = 0 #불일치도의 최댓값
prev_dp, new_dp = [0]*(len(s)+1), [0]*(len(s)+1) #앞부분, 뒷부분
for i in range(len(s)):
    new = s[i] #새로 생기는 문자
    for j in range(len(s)-1, -1, -1):
        if new == s[j]:
            new_dp[j] = prev_dp[j+1] + 1
        else:
            new_dp[j] = max(prev_dp[j], new_dp[j+1])
    split_p = i+1
    lcs = new_dp[split_p]
    ans = max(ans, min(split_p, len(s)-split_p) - lcs) #불일치도 계산 수식
    prev_dp, new_dp = new_dp, prev_dp #swap해서 재사용

print(ans)