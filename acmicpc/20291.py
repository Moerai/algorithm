# Problem
"""
친구로부터 노트북을 중고로 산 스브러스는 노트북을 켜자마자 경악할 수밖에 없었다.
바탕화면에 온갖 파일들이 정리도 안 된 채 가득했기 때문이다.
그리고 화면의 구석에서 친구의 메시지를 확인할 수 있었다.

바탕화면의 파일들에는 값진 보물에 대한 정보가 들어 있어.
하나라도 지우게 된다면 보물은 물론이고 다시는 노트북을 쓸 수 없게 될 거야.
파일들을 잘 분석해서 보물의 주인공이 될 수 있길 바랄게. 힌트는 “확장자”야.

화가 났던 스브러스는 보물 이야기에 금세 화가 풀렸고 보물의 정보를 알아내려고 애썼다.
하지만 파일이 너무 많은 탓에 이내 포기했고 보물의 절반을 보상으로 파일의 정리를 요청해왔다.
스브러스의 요청은 다음과 같다.

파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘
보기 편하게 확장자들을 사전 순으로 정렬해 줘
그럼 보물의 절반을 얻어내기 위해 얼른 스브러스의 노트북 파일 정리를 해줄 프로그램을 만들자!
"""

# Input
"""
첫째 줄에 바탕화면에 있는 파일의 개수 N이 주어진다. (1 <= N <= 50,000)
둘째 줄부터 $N$개 줄에 바탕화면에 있는 파일의 이름이 주어진다. 파일의 이름은 알파벳 소문자와 점(.)으로만 구성되어 있다.
점은 정확히 한 번 등장하며, 파일 이름의 첫 글자 또는 마지막 글자로 오지 않는다. 각 파일의 이름의 길이는 최소 $3$, 최대 $100$이다.
"""

# Output
"""
확장자의 이름과 그 확장자 파일의 개수를 한 줄에 하나씩 출력한다.
확장자가 여러 개 있는 경우 확장자 이름의 사전순으로 출력한다.
"""

# Example
"""
|Input|
8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
|Output|
icpc 2
spc 2
txt 3
world 1
"""

# Solution
import sys
input = sys.stdin.readline
n = int(input())
fe = {}

for i in range(n):
    s = input()
    index = s.find('.')
    s = s[index+1:]
    if s in fe:
        fe[s] += 1
    else:
        fe[s] = 1

for result in sorted(fe):
    print(result, fe[result])

# Solution2
import sys
input = sys.stdin.readline

n = int(input())

file = dict()
for _ in range(n):
    extend = (input().split('.'))[1]
    if not extend in file:
        file[extend] = 1
    else:
        file[extend] += 1

sort_file = sorted(file.items())

for key, value in sort_file:
    print(key.rstrip(), value)