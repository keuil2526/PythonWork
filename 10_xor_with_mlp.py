#퍼셉트론=
#입력값 두개일때 두개다 참이여야 참임. and조건
# 그리고 편향을 준다. 데이터 값에 따라 weight가 붙는다. 
# weight를 바꿔가는 걸 deep learning이라고 한다.
#스스로 찾아내는게 weight와 bias를 찾아내는것
#전체 데이터에 weight를 게산하고 마지막에 bias를 더한다.
#bsms 위아래로 움직이는거 weight는 기울기
#learning rate는 weight를 얼마나 바꿀지 결정하는 값
#learning rate가 너무 크면 발산 또는 진동
#learning rate가 너무 작으면 학습이 느려짐
#활성 함수 
def step(z):
    if z>=0:
        return 1
    return 0
#z: 활성화 함수 
#퍼셉트론 
def perceptron(x1,x2,w1,w2,b):
    result= x1*w1+x2*w2+b
    return step(result)

#AND gate( 입력값 두개일때 두개다 참이여야 참임. and조건)
def AND(x1, x2):
    return perceptron(x1, x2, w1=0.5 , w2=0.5 , b=-0.7)

#OR gate
def OR(x1, x2):
    return perceptron(x1, x2, w1=0.5 , w2=0.5 , b=-0.2)

#NAND gate
def NAND(x1, x2):
    return perceptron(x1, x2, w1=-0.5 , w2=-0.5 , b=0.7)



#XOR
def XOR(x1, x2):
    hidden1 = OR(x1, x2) #OR gate
    hidden2 = NAND(x1, x2) #NAND gate

    ouput = AND(hidden1, hidden2) #AND gate

    print(f'Output Layer And({hidden1}, {hidden2}) -> {ouput}')
    return ouput

#입력 데이터 
data =[(0,0),(0,1),(1,0),(1,1)]

for x1,x2 in data:
    print(f'{x1}{x2} -> {XOR(x1,x2)}')