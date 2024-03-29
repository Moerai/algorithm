# Problem
"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""

# Input
"""
첫 줄에 수의 개수 N이 주어진다.
N은 100이하이다.
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
"""

# Output
"""
주어진 수들 중 소수의 개수를 출력한다.
"""

# Example
"""
|Input|
4
1 3 5 7
|Output|
3
"""

# Solution
import math

n = int(input())
numbers = map(int, input().split())
count = 0

for number in numbers:
    flag = True
    if number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                flag = False
        if flag == True:
            count += 1

print(count)