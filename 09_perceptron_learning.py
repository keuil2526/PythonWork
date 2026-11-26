import random

#Step_Function
def step(z):
    if z >= 0:
        return 1
    return 0

#Train_Data
train_data = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1)
]

#Weight_Setting
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
b = random.uniform(-1, 1)

#Learn_Setting
learning_rate = 0.1
epochs = 30

print(f'w1 = {w1:.3f}, w2 = {w2:.3f}, b = {b:.3f}')
print()

#Learn
for epoch in range(epochs):
    total_error = 0

    for x1, x2, target in train_data:
        y = step(x1 * w1 + x2 * w2 + b)
        error = target - y
        total_error += abs(error)

        print(f'x1 = {x1}, x2 = {x2}')
        print(f'target = {target}, predict = {y}, error = {error}')

        #Weight_Update
        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        b += learning_rate * error

    print()
    print(f'Epoch {epoch + 1:2d} | total_error = {total_error}')
    print(f'w1 = {w1:.3f}, w2 = {w2:.3f}, b = {b:.3f}')
    print()

    if total_error == 0:
        print('Learn Completed')
        break

#Result
print('Final Result')

for x1, x2, target in train_data:
    y = step(x1 * w1 + x2 * w2 + b)
    print(f'{x1}, {x2} -> Predict: {y}, Answer: {target}')

print()
print(f'Final Weight: w1 = {w1:.3f}, w2 = {w2:.3f}')
print(f'Final Bias: b = {b:.3f}')
