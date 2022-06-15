import tensorflow as tf
mnist = tf.keras.datasets.mnist

print("-----------P22-----------")


# Laden des MNIST Datasets, siehe Aufgaben vorher. Integernummern werden mit der Divison zu Floating-Point Zahlen umgewandelt.
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

### ... (Kommentar einfügen) ...
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
### ... (Kommentar einfügen) ...
predictions = model(x_train[:1]).numpy()
### ... (Kommentar einfügen) ...
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
### ... (Kommentar einfügen) ...
model.compile(
optimizer='adam',
loss=loss_fn,
metrics=['accuracy']
)
### ... (Kommentar einfügen) ...
model.fit(x_train, y_train, epochs=5)

### P23
print("-----------P23-----------")

### ... (Kommentar einfügen) ...
model.evaluate(x_test, y_test, verbose=2)
probability_model = tf.keras.Sequential([
model,
tf.keras.layers.Softmax()
])
### ... (Kommentar einfügen) ...
print(y_test[:1])
### ... (Kommentar einfügen) ...
probability_model(x_test[:1])
