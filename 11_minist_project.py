import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#Text_Print_With_Line
def printer(text):
    print()
    print('='*10, text, '='*10)
    print()
    
#Load_MNIST_Dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

#View_Dataset_Shape
print(f"x_train shape : {x_train.shape}")
print(f"y_train shape : {y_train.shape}")
print(f"x_test shape : {x_test.shape}")
print(f"y_test shape : {y_test.shape}")

#View_First_Image
plt.figure(figsize=(5,5))
plt.imshow(x_train[0], cmap='gray')
plt.title(f"Label : {y_train[0]}")
plt.axis('off')
plt.show()

print(x_train[0][:, :])
print()

#Data_Regularization
x_train = x_train / 255.0
x_test = x_test / 255.0
print(x_train[0][:, :])
print()

#Flatten_Data
x_train = x_train.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)

print(x_train[0][:])
print()

#Make_Neural_Network_Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(28 * 28,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
print('Model Summary')
print(model.summary())

#Model_compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
print('Model Compile Completed')

#Train_Model
history = model.fit(x_train, y_train, epochs=5, validation_split=0.2, batch_size=32, verbose=1)
print('Model Training Completed')
print(history.history.keys())

#Check_loss_and_accuracy_and_validation
plt.figure(figsize=(12, 5))

#loss_plot
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss', marker='o')
plt.plot(history.history['val_loss'], label='Validation Loss', marker='s')
plt.title('Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)

#accuracy_plot
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='s')
plt.title('Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#Check_Test_Accuracy
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
printer("Test Result")
print(f"Test Loss : {loss:.4f}")
print(f"Test Accuracy : {accuracy:.4f}")
print()

#New_Data_Prediction
predictions = model.predict(x_test[:1])
printer('Prediction Ratios')
print(predictions)
print()

#Check_Predicted_Data
predicted_number = np.argmax(predictions)
printer('Predicted Number')
print(f"Predicted Number : {predicted_number}")
print(f"Actual Number : {y_test[0]}")
print()

#Compare_Predicted_and_Actual
plt.figure(figsize=(5, 5))
plt.imshow(x_test[0].reshape(28, 28), cmap='gray')
plt.title(f"Predicted : {predicted_number}, Actual : {y_test[0]}")
plt.axis('off')
plt.show()

#Many_Data_Prediction
predictions = model.predict(x_test[:10])
predicted_labels = np.argmax(predictions, axis=1)
printer('Predicted Labels')
for i in range(10):
    print(f"No.{i+1}")
    print(f"Predicted : {predicted_labels[i]}, Actual : {y_test[i]}")
    print()

#Visualize_Predictions
plt.figure(figsize=(12, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Predicted : {predicted_labels[i]}\nActual : {y_test[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()