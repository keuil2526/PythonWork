import random

def step(z):
    return 1 if z>=0 else 0
#학습 데이터: 데이터와 정답
train_data=[
    (0,0,0),
    (0,1,0),
    (1,0,0),
    (1,1,1),
]

#가중치 초기화
w1= random.uniform(-1,1)
w2= random.uniform(-1,1)
b= random.uniform(-1,1)

#가중치, 편향 수정 정도
learning_rate=0.1
#학습 반복 횟수
epoch=30
print(f'w1={w1:.3f}, w2={w2:.3f}, b={b:.3f}')
print()

#학습 시작
for epoch in range(epoch):
    total_error=0
    for x1, x2, target in train_data:
        print(f'x1={x1}, w1={w1:.3f}, x2={x2}, w2={w2:.3f}, b={b:.3f}')
        #예측값 계산
        y=step(x1*w1+x2*w2+b)

        #오차값(실질값-예측값)
        error=target-y
        print(f'target:{target}, y:{y}, error:{error}')

        total_error+= abs(error) #total_error + abs(error)

        #퍼셉트론 학습 규칙: 입력값이 1인 곳과 b값만 수정
        #가중치, 편향 수정
        w1 += learning_rate*error*x1
        w2 += learning_rate*error*x2
        b += learning_rate*error
        #타겟은 실질값, 예측값은y
        #x1, x2가 입력값.
    print(f'Epoch {epoch+1:2d} | 'f'total_error={total_error} | 'f'w1={w1:.3f} 'f'w2={w2:.3f} 'f'b={b:.3f} ')
    print()
    
    if total_error == 0 :
        print('Learn Completed')
        break

for x1, x2, target in train_data :
    y = step(x1 * w1 + x2 * w2 + b)
    print(f'{x1}, {x2}' f'Predict : {y}' f'Answer : {target}')
    print()
    print(f'Final Weight, Bias : w1={w1:.3f}, w2={w2:.3f}, b={b:.3f}')