# 퍼셉트론
# 입력값에 가중치를 곱하고 편향을 더한 뒤 활성화 함수로 결과를 결정한다.
# 가중치와 편향을 조절하면 원하는 논리 게이트를 만들 수 있다.

# 계단 함수
def step(z):
    if z >= 0:
        return 1
    return 0


# 퍼셉트론
def perceptron(x1, x2, w1, w2, b):
    result = x1 * w1 + x2 * w2 + b
    return step(result)


# AND 게이트
def AND(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.7)


# OR 게이트
def OR(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.2)


# NAND 게이트
def NAND(x1, x2):
    return perceptron(x1, x2, -0.5, -0.5, 0.7)


# 입력 데이터
data = [(0, 0), (0, 1), (1, 0), (1, 1)]


# AND 게이트 결과
print('AND')
for x1, x2 in data:
    print(f'{x1}, {x2} -> {AND(x1, x2)}')

# OR 게이트 결과
print()
print('OR')
for x1, x2 in data:
    print(f'{x1}, {x2} -> {OR(x1, x2)}')

# NAND 게이트 결과
print()
print('NAND')
for x1, x2 in data:
    print(f'{x1}, {x2} -> {NAND(x1, x2)}')
