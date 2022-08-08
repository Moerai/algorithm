# Problem
"""
알파벳 소문자로 이루어진 문자열 S와 단어 목록 A가 주어졌을 때,
S를 A에 포함된 문자열을 한 개 이상 공백없이 붙여서 만들 수 있는지 없는지 구하는 프로그램을 작성하시오.
A에 포함된 단어를 여러 번 사용할 수 있다.
"""

# Input
"""
첫째 줄에 길이가 100이하인 문자열 S가 주어진다.
둘째 줄에는 A에 포함된 문자열의 개수 N(1 ≤ N ≤ 100)이 주어진다.
셋째 줄부터 N개의 줄에는 A에 포함된 단어가 한 줄에 하나씩 주어진다.
A에 포함된 문자열은 알파벳 소문자로만 이루어져 있고, 길이는 100을 넘지 않는다.
"""

# Output
"""
A에 포함된 문자열로 S를 만들 수 있으면 1, 없으면 0을 출력한다.
"""

# Example
"""
|Input1|
softwarecontest
2
software
contest
|Output1|
1
"""

# Solution
def sol(idx):
    global result
    if idx == len(S):
        result = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1
    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]):
            for j in range(len(A[i])):
                if A[i][j] != S[idx+j]:
                    break
            else:
                sol(idx+len(A[i]))
    return
    
S = input()
A = []
dp = [0] * 101
for _ in range(int(input())):
    A.append(input())
result = 0
sol(0)
print(result)