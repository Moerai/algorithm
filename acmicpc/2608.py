# Problem
"""
로마 시대 때는 현재 사용하는 아라비아 숫자가 아닌 다른 방법으로 수를 표현하였다.
로마 숫자는 다음과 같은 7개의 기호로 이루어진다.

기호	 I 	 V 	 X	 L 	 C	 D	 M
값  	1	5	10	50	100	500	1000
수를 만드는 규칙은 다음과 같다.

1. 보통 큰 숫자를 왼쪽에 작은 숫자를 오른쪽에 쓴다. 그리고 그 값은 모든 숫자의 값을 더한 값이 된다.
예를 들어 LX = 50 + 10 = 60 이 되고, MLI = 1000 + 50 + 1 = 1051 이 된다.

2. V, L, D는 한 번만 사용할 수 있고 I, X, C, M은 연속해서 세 번까지만 사용할 수 있다.
예를 들어 VV나 LXIIII 와 같은 수는 없다. 그리고 같은 숫자가 반복되면 그 값은 모든 숫자의 값을 더한 값이 된다.
예를 들어 XXX = 10 + 10 + 10 = 30 이 되고, CCLIII = 100 + 100 + 50 + 1 + 1 + 1 = 253 이 된다.

3. 작은 숫자가 큰 숫자의 왼쪽에 오는 경우는 다음과 같다. IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900 을 나타낸다.
이들 각각은 한 번씩만 사용할 수 있다. 그런데 IV 와 IX 는 같이 쓸 수 없으며 XL 과 XC, CD 와 CM 또한 같이 쓸 수 없다.
이들 외에는 작은 숫자가 큰 숫자 왼쪽 어디에도 나올 수 없다.
예를 들어 XCXC 나 CMCD, VX 나 IIX 와 같은 수는 없다. 참고로 LIX = 50 + 9 = 59, CXC = 100 + 90 = 190 이 된다.

4. 모든 수는 가능한 가장 적은 개수의 로마 숫자들로 표현해야 한다. 예를 들어 60 은 LX 이지 XLXX 가 아니고, 5 는 V 이지 IVI 가 아니다.

아래의 예를 참고 하시오.

- DLIII = 500 + 50 + 3 = 553
- MCMXL = 1000 + 900 + 40 = 1940
- 235 = CCXXXV
- 2493 = MMCDXCIII
로마 숫자로 이루어진 두 수를 입력받아 그 둘을 더한 값을 아라비아 숫자와 로마 숫자로 출력하는 프로그램을 작성하시오.
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
s1 = input()
s2 = input()

sign = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
sign2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

def to_num(s):
    l=len(s)
    num =0
    visited = [0]*l
    for i in range(l):
        if visited[i]==0:
            if i+1<len(s) and s[i:i+2] in sign2.keys():
                visited[i], visited[i+1] =1,1
                num += int(sign2[s[i:i+2]])
            else:
                visited[i]=1
                num+=int(sign[s[i]])
    return num

def to_str(n):
    s=""
    while n>0:
        if n>=1000:
            s+="M"
            n-=1000
        elif n>=900:
            s+="CM"
            n-=900
        elif n>=500:
            s+="D"
            n-=500
        elif n>=400:
            s+="CD"
            n-=400
        elif n>=100:
            s+="C"
            n-=100
        elif n>=90:
            s+="XC"
            n-=90
        elif n>=50:
            s+="L"
            n-=50
        elif n>=40:
            s+="XL"
            n-=40
        elif n>=10:
            s+="X"
            n-=10
        elif n>=9:
            s+="IX"
            n-=9
        elif n>=5:
            s+="V"
            n-=5
        elif n>=4:
            s+="IV"
            n-=4
        elif n>=1:
            s+="I"
            n-=1
    return s

nresult = to_num(s1)+to_num(s2)
print(nresult)
print(to_str(nresult))