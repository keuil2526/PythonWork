#Step_Function
def step(z):
    if z >= 0:
        return 1
    return 0

#Perceptron
def perceptron(x1, x2, w1, w2, b):
    result = x1 * w1 + x2 * w2 + b
    return step(result)

#AND
def AND(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.7)

#OR
def OR(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.2)

#NAND
def NAND(x1, x2):
    return perceptron(x1, x2, -0.5, -0.5, 0.7)

#XOR
def XOR(x1, x2):
    hidden1 = OR(x1, x2)
    hidden2 = NAND(x1, x2)

    output = AND(hidden1, hidden2)

    print(f'Output: AND({hidden1}, {hidden2}) -> {output}')
    return output

#Data
data = [(0, 0), (0, 1), (1, 0), (1, 1)]

#Result
for x1, x2 in data:
    print(f'{x1}, {x2} -> {XOR(x1, x2)}')
