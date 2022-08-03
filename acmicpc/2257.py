# Problem
"""
우리가 널리 사용하는 H2O(물), CH3COOH(아세트산)과 같은 화학식은 알파벳과 숫자, 그리고 괄호로 구성된다.
먼저 알파벳은 원자를 나타내는 것으로 H는 수소(Hydrogen), C는 탄소(Carbon), O는 산소(Oxygen) 원자를 뜻한다.
또한 원자를 나타내는 알파벳 뒤에 따르는 숫자는 그 원자가 몇 개 포함되어 있는지를 뜻한다. 따라서 COOHHH 분자는 CO2H3로 나타낼 수 있다.
이 문제에서, 숫자는 항상 2 이상 9 이하로만 입력으로 주어진다. 따라서 CO23과 같이 숫자가 두자리인 경우는 없다.

물의 화학식을 보고 물은 두 개의 수소 원자와 한 개의 산소 원자로 이루어졌음을 알 수 있다.
또한 아세트산의 화학식처럼 한 종류의 알파벳이 화학식에 여러 번 나타날 수도 있다.
실제 화학식 또한 이렇게 사용되는데, 이는 분자의 결합 구조를 나타내기 위함이다.

종종 화학식에는 괄호가 사용되기도 하는데 괄호로 묶인 원자들은 하나의 새로운 원자와 같은 작용을 한다.
따라서 CH(CO2H)(CO2H)(CO2H) 분자는 CH(CO2H)3와 같이 나타낼 수 있다.
괄호 안에 아무런 알파벳도 없는 경우도 있을 수 있는데, 이런 경우는 괄호가 없는 경우와 마찬가지라고 생각하면 된다.

이러한 화학식을 보고 우리는 화학식량을 계산할 수 있는데, 화학식량이란 그 화학식에 포함되어 있는 모든 원자들의 질량의 합을 말한다.
수소 원자 하나의 질량은 1, 탄소 원자 하나의 질량은 12, 산소 원자 하나의 질량은 16이다.
물은 두 개의 수소 원자와 한 개의 산소 원자로 이루어져 있으므로 물의 화학식량은 18이다.

화학식이 주어졌을 때, 이 화학식의 화학식량을 계산하는 프로그램을 작성하시오.
화학식은 수소, 탄소, 산소만을 포함하고 있는 것만이 입력으로 주어진다.
"""

# Input
"""
첫째 줄에 화학식이 주어진다. 화학식은 H, C, O, (, ), 2, 3, 4, 5, 6, 7, 8, 9만으로 이루어진 문자열이며, 그 길이는 100을 넘지 않는다.
"""

# Output
"""
첫째 줄에 화학식량을 출력한다. 분자량이 10,000이 넘는 고분자는 입력으로 주어지지 않는다.
"""

# Example
"""
|Input1|
(H)2(O)
|Output1|
18

|Input2|
CH(CO2H)3
|Output2|
148

|Input3|
((CH)2(OH2H)(C(H))O)3
|Output3|
222
"""

# Solution
chemical_formula = input()
stack = []
atom = {'H':1, 'C':12, 'O':16}
for chemical in chemical_formula:
    if chemical=='(':
        stack.append(chemical)
    elif chemical=='H' or chemical=='C' or chemical=='O':
        stack.append(atom[chemical])
    elif chemical==')':
        temp = 0
        while True:
            if stack[-1]== '(':
                stack.pop()
                stack.append(temp)
                break
            else:
                temp+=stack.pop()
    else:
        stack.append(stack.pop()*int(chemical))

print(sum(stack))
