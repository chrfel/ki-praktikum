import tensorflow as tf
mnist = tf.keras.datasets.mnist

print("-----------P22-----------")


# Laden des MNIST Datasets, siehe Aufgaben vorher. Integernummern werden mit der Divison zu Floating-Point Zahlen umgewandelt.
(x_train, y_train), (x_test, y_test) = mnist.load_data() ## x enthaelt das Bild und y das Ergebnis
x_train, x_test = x_train / 255.0, x_test / 255.0

### Strukturiere das neuronale Netz und NN2, relu, selu und sigmoid
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),## Informationen der Bilder werden in 28x28 gespeichert, und durchs Flatten in einem eindimensionalen Vektor gespeichert
  tf.keras.layers.Dense(128, activation='relu'), ## Erstellt eine Ebene mit 128 Neuronen, die mit allen Neuronen der folgenden und vorherigen Ebene vollständig biparit verbunden wird
  tf.keras.layers.Dropout(0.3), ## Jedes Neuron hat eine 20% Chance auf jeden Fall 0 auszugeben, um dem Overfitting entgegenzuwirken
  tf.keras.layers.Dense(10) ## Erstellt eine Ebene mit 10 Neuronen, Output Layer, Activation ist linear a(x) = x
])

### NN1 Ohne Hidden Layer
# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),## Informationen der Bilder werden in 28x28 gespeichert, und durchs Flatten in einem eindimensionalen Vektor gespeichert
#   tf.keras.layers.Dense(10) ## Erstellt eine Ebene mit 10 Neuronen, Output Layer, Activation ist linear a(x) = x
# ])

### NN3
# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),## Informationen der Bilder werden in 28x28 gespeichert, und durchs Flatten in einem eindimensionalen Vektor gespeichert
#   tf.keras.layers.Dense(128, activation='relu'), ## Erstellt eine Ebene mit 128 Neuronen, die mit allen Neuronen der folgenden und vorherigen Ebene vollständig biparit verbunden wird
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(4, activation='relu'),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dropout(0.2), ## Jedes Neuron hat eine 20% Chance auf jeden Fall 0 auszugeben, um dem Overfitting entgegenzuwirken
#   tf.keras.layers.Dense(10) ## Erstellt eine Ebene mit 10 Neuronen, Output Layer, Activation ist linear a(x) = x
# ])

### Probe mit einem Testwert
predictions = model(x_train[:1]).numpy()
### Probe ueberpruefen
tf.nn.softmax(predictions).numpy() ## Sorgt fuer Prozentwerte
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
### Das Model konfigurieren
model.compile(
optimizer='adam',
loss=loss_fn,
metrics=['accuracy']
)
### Training mit Testdaten, 5 * alle Datensaetze
model.fit(x_train, y_train, epochs=5) ## Loss gibt die Performance des Models an und Accuracy die Genauigkeit an

### P23
print("-----------P23-----------")

### Das trainierte Model mit den Testdaten ueberpruefen und fuegt dann dem Model noch Softmax zur besseren Ausgabe an
model.evaluate(x_test, y_test, verbose=2) ##Verbose gibt die Art der Ausgabe an
probability_model = tf.keras.Sequential([
model,
tf.keras.layers.Softmax()
])
### Printet das reale Ergebnis des ersten Tests
print(y_test[:1])
### Printet das berechnete Ergebnis Vektor des ersten Tests
print(probability_model(x_test[:1]))
