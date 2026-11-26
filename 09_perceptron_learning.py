import random


# 계단 함수
def step(z):
    if z >= 0:
        return 1
    return 0


# 학습 데이터: 입력값 두 개와 정답
train_data = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1)
]


# 가중치와 편향 초기화
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
b = random.uniform(-1, 1)

# 학습 설정
learning_rate = 0.1
epochs = 30

print(f'w1 = {w1:.3f}, w2 = {w2:.3f}, b = {b:.3f}')
print()


# 퍼셉트론 학습
for epoch in range(epochs):
    total_error = 0

    for x1, x2, target in train_data:
        # 예측값 계산
        y = step(x1 * w1 + x2 * w2 + b)

        # 오차 계산
        error = target - y
        total_error += abs(error)

        print(f'x1 = {x1}, x2 = {x2}')
        print(f'target = {target}, predict = {y}, error = {error}')

        # 가중치와 편향 수정
        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        b += learning_rate * error

    print()
    print(f'Epoch {epoch + 1:2d} | total_error = {total_error}')
    print(f'w1 = {w1:.3f}, w2 = {w2:.3f}, b = {b:.3f}')
    print()

    # 모든 데이터를 맞히면 학습 종료
    if total_error == 0:
        print('Learn Completed')
        break


# 학습 결과 확인
print('Final Result')

for x1, x2, target in train_data:
    y = step(x1 * w1 + x2 * w2 + b)
    print(f'{x1}, {x2} -> Predict: {y}, Answer: {target}')

print()
print(f'Final Weight: w1 = {w1:.3f}, w2 = {w2:.3f}')
print(f'Final Bias: b = {b:.3f}')
