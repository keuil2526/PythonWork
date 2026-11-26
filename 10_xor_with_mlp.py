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


# XOR 게이트
# 은닉층에서 OR과 NAND를 계산하고 출력층에서 AND를 계산한다.
def XOR(x1, x2):
    hidden1 = OR(x1, x2)
    hidden2 = NAND(x1, x2)

    output = AND(hidden1, hidden2)

    print(f'Output: AND({hidden1}, {hidden2}) -> {output}')
    return output


# 입력 데이터
data = [(0, 0), (0, 1), (1, 0), (1, 1)]


# XOR 결과 확인
for x1, x2 in data:
    print(f'{x1}, {x2} -> {XOR(x1, x2)}')
