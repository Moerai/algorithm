# Problem
"""
팰린드롬은 어느 방향으로 읽어도 항상 같은 방법으로 읽을 수 있는 단어이다. 예를 들어, civic, radar, rotor, madam은 팰린드롬이다.
상근이는 단어 k개 적혀있는 공책을 발견했다.
공책의 단어는 ICPC 문제가 저장되어 있는 서버에 접속할 수 있는 비밀번호에 대한 힌트이다.
비밀번호는 k개의 단어 중에서 두 단어를 합쳐야 되고, 팰린드롬이어야 한다.
예를 들어, 단어가 aaba, ba, ababa, bbaa, baaba일 때, ababa와 ba를 합치면 팰린드롬 abababa를 찾을 수 있다.
단어 k개 주어졌을 때, 팰린드롬을 찾는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스의 첫째 줄에는 공책에 적혀져있는 단어의 수 k(1 ≤ k ≤ 100)가 주어진다.
다음 k개 줄에는 a부터 z까지 알파벳으로 이루어진 단어가 한 줄에 하나씩 주어진다. 모든 단어 길이의 합은 10,000보다 작거나 같다.
"""

# Output
"""
각 테스트 케이스마다 팰린드롬을 출력한다. 만약, 가능한 팰린드롬이 여러 가지라면 아무거나 출력한다. 팰린드롬을 만들 수 없는 경우에는 0을 출력한다.
"""

# Example
"""
|Input1|
2
5
aaba
ba
ababa
bbaa
baaba
3
abc
bcd
cde
|Output1|
abababa
0
"""

# Solution
for _ in range(int(input())):
    n = int(input())
    w = [input() for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                pass
            else:
                res = w[i] + w[j]
                a = 0
                for k in range(len(res)//2+1):
                    if res[k] != res[-(k+1)]:
                        a = 1
                        break
                if a == 0:
                    print(res)
                    cnt += 1
                    break
        if cnt == 1:
            break
    if cnt == 0:
        print('0')