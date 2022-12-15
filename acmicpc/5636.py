# Problem
"""
숫자로 이루어진 문자열이 주어진다. 이때, 부분 문자열 중에서 가장 큰 소수를 찾는 프로그램을 작성하시오.
이 문제에서는 2보다 크거나 같고, 100,000보다 작거나 같은 소수만 소수이다.
"""

# Input
"""
입력은 여러 개의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 1,000개를 넘지 않는다.
각 테스트 케이스는 길이가 255를 넘지 않는 숫자 문자열로 이루어져 있다. 입력의 마지막 줄에는 0이 하나 주어진다.
"""

# Output
"""
각 테스트 케이스에 대해서, 가장 큰 소수 부분 문자열을 출력한다. 
"""

# Example
"""
|Input1|
11245
91321150448
1226406
0
|Output1|
11
1321
2
"""

# Solution
# 부분문자열을 뽑고 소수인지 판별해서 리스트에 넣고 max출력