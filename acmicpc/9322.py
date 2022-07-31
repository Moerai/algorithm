# Problem
"""
소희는 공개키와 개인키 한 쌍으로 보안을 유지하는 것이 매우 불편하다고 생각했다.
그래서 소희는 공개키만을 이용하는 암호화 체계를 개발했다. 이를 "철벽 보안 알고리즘"이라고 부르기로 했다. 알고리즘은 다음과 같다.
한 단어는 1~10개의 대문자(A-Z)들로 이루어진 문자열이다. 한 문장은 공백으로 구분된 단어들로 이루어졌다.
제 1 공개키는 최대 한 번만 사용된 단어들로 되어있다.
제 2 공개키는 제 1 공개키의 단어들을 재배치하여 만들어진다.
평문(암호화 되지 않은 문장)은 제 1 공개키와 같이 여러 단어들로 되어있지만, 제 1 공개키와 다르게 각 단어들은 중복이 가능하다.
암호문(암호화 된 문장)은 평문을 제 2 공개키를 만든 규칙의 반대로 재배치하여 만들어진다.
주어진 2개의 공개키와 암호문으로 평문을 복구하라.
"""

# Input
"""
입력의 첫 줄에는 테스트 케이스의 수를 의미하는 하나의 정수가 입력된다. 정수는 100을 넘지 않는다.
각 테스트케이스마다 아래 항목들을 한 줄씩 입력받는다.
- 한 문장의 단어 수 n (1 ≤ n ≤ 1 000)
- 제 1 공개키
- 제 2 공개키
- 암호문
모든 단어들은 최소 1개, 최대 10개의 대문자들로 이루어져있다.
"""

# Output
"""
각 케이스마다
- 암호문을 해독한 평문
을 한 줄에 줄력한다.
"""

# Example
"""
|Input1|
2
4
A B C D
D A B C
C B A P
3
SECURITY THROUGH OBSCURITY
OBSCURITY THROUGH SECURITY
TOMORROW ATTACK WE
|Output|
B A P C
WE ATTACK TOMORROW
"""
# Solution
m = int(input())

for i in range(m):
    n = int(input())
    fi = input().split()
    scnd = input().split()
    pwd = input().split()

    index_list = []
    for i in fi:
        index_list.append(scnd.index(i))
    
    answer = []
    for i in index_list:
        answer.append(pwd[i])
    
    print(*answer)