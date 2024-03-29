# Problem
"""
개미가 일렬로 이동할 때, 가장 앞의 개미를 제외한 나머지 개미는 모두 앞에 개미가 한 마리씩 있다. 
서로 반대 방향으로 이동하던 두 개미 그룹이 좁은 길에서 만났을 때, 개미는 어떻게 지나갈까?
최근 연구에 의하면 위와 같은 상황이 벌어지면 개미는 서로를 점프해서 넘어간다고 한다.
즉, 두 그룹이 만났을 때, 1초에 한번씩 개미는 서로를 뛰어 넘는다. (한 개미가 다른 개미를 뛰어 넘고, 다른 개미는 그냥 전진한다고 생각해도 된다)
하지만 모든 개미가 점프를 하는 것은 아니다. 자신의 앞에 반대 방향으로 움직이던 개미가 있는 경우에만 점프를 하게 된다.
첫 번째 그룹이 ABC로 움직이고, 두 번째 그룹의 개미가 DEF순으로 움직인다고 하자.
그럼, 좁은 길에서 만났을 때, 개미의 순서는 CBADEF가 된다.
1초가 지났을 때는 자신의 앞에 반대방향으로 움직이는 개미가 있는 개미는 A와 D다. 따라서, 개미의 순서는 CBDAEF가 된다.
2초가 되었을 때, 자신의 앞에 반대 방향으로 움직이는 개미는 B,D,A,E가 있다. 따라서, 개미의 순서는 CDBEAF가 된다.
T초가 지난 후에 개미의 순서를 구하는 프로그램을 작성하시오.
"""

# Input
"""
첫 번째 줄에 첫 번째 그룹의 개미의 수 N1과 두 번째 그룹의 개미의 수 N2가 주어진다.
다음 두 개 줄에는 첫 번째 그룹과 두 번째 그룹의 개미의 순서가 주어진다. 각 개미는 알파벳 대문자로 표현할 수 있으며, 두 그룹에서 중복되는 알파벳은 없다.
마지막 줄에는 T가 주어진다. (0 ≤ T ≤ 50)
"""

# Output
"""
T초가 지난 후에 개미의 순서를 출력한다. 첫 번째 개미 그룹은 왼쪽에서 오른쪽으로 움직이고, 두 번째 그룹은 반대 방향으로 움직인다.
"""

# Example
"""
|Input1|
3 3
ABC
DEF
0
|Output1|
CBADEF

|Input2|
3 3
ABC
DEF
2
|Output2|
CDBEAF

|Input3|
3 4
JLA
CRUO
3
|Output3|
CARLUJO
"""

# Solution
n1, n2 = map(str, input().split())
ant1 = list(input())
ant2 = list(input())
t = int(input())

ant_all = ant1[::-1] + ant2

for i in range(t):
    for i in range(len(ant_all)-1):
        if ant_all[i] in ant1 and ant_all[i+1] in ant2:
            ant_all[i], ant_all[i+1] = ant_all[i+1], ant_all[i]
            if ant_all[i+1] == ant1[0]:
                break
print(''.join(ant_all))