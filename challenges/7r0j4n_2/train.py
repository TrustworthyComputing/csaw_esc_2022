import tensorflow as tf
import larq as larq

"""
Import CIFAR10 Dataset
We download and normalize the CIFAR10 dataset.
"""

num_classes = 10

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

train_images = train_images.reshape((50000, 32, 32, 3)).astype("float32")
test_images = test_images.reshape((10000, 32, 32, 3)).astype("float32")

# Normalize pixel values to be between -1 and 1
train_images, test_images = train_images / 127.5 - 1, test_images / 127.5 - 1

train_labels = tf.keras.utils.to_categorical(train_labels, num_classes)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes)

"""
Build BinaryNet

Here we build the BinaryNet model layer by layer using the [Keras Sequential API](https://www.tensorflow.org/guide/keras).
"""

# All quantized layers except the first will use the same options
kwargs = dict()

model = tf.keras.models.Sequential([
    # In the first layer we only quantize the weights and not the input
    tf.keras.layers.Conv2D(128, 3,
                          use_bias=False,
                          input_shape=(32, 32, 3)),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Conv2D(128, 3, padding="same", **kwargs),
   
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Conv2D(256, 3, padding="same", **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Conv2D(256, 3, padding="same", **kwargs),
    
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Conv2D(512, 3, padding="same", **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Conv2D(512, 3, padding="same", **kwargs),
    
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.Flatten(),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(1024, **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(1024, **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),

    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(1024, **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(1024, **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(10, **kwargs),
    tf.keras.layers.Activation("softmax")
])

# One can output a summary of the model
larq.models.summary(model)

"""
Model Training

Compile the model and train the model
"""

model.compile(
    tf.keras.optimizers.Adam(lr=0.01, decay=0.0001),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

trained_model = model.fit(
    train_images, 
    train_labels,
    batch_size=50, 
    epochs=1,
    validation_data=(test_images, test_labels),
    shuffle=True
)

for i in range(10):
    model.save_weights("FullNetwork_" + str(i))
    trained_model = model.fit(
        train_images, 
        train_labels,
        batch_size=50, 
        epochs=10,
        validation_data=(test_images, test_labels),
        shuffle=True
    )

model.save_weights("FullNetwork")
